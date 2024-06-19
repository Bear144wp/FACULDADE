import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from sqlalchemy import or_
from database import get_session, Truck

class TruckRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Aluguel de Caminhões")
        self.root.state('zoomed')  # Tela cheia

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=10)
        self.style.configure("TLabel", font=("Arial", 14))
        self.style.configure("TEntry", font=("Arial", 12))

        self.name_var = tk.StringVar()
        self.year_var = tk.StringVar()
        self.value_var = tk.StringVar()
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.search_trucks)

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True, fill=tk.BOTH)

        title = ttk.Label(frame, text="Sistema de Aluguel de Caminhões", font=("Arial", 24, "bold"))
        title.grid(row=0, column=0, columnspan=4, pady=20)

        ttk.Label(frame, text="Nome:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(frame, textvariable=self.name_var, width=30).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ano:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(frame, textvariable=self.year_var, width=30).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Valor:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(frame, textvariable=self.value_var, width=30).grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Adicionar Caminhão", command=self.add_truck).grid(row=4, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Pesquisar:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(frame, textvariable=self.search_var, width=30).grid(row=5, column=1, padx=5, pady=5)

        self.trucks_listbox = tk.Listbox(frame, width=80, height=20, font=("Arial", 12))
        self.trucks_listbox.grid(row=6, column=0, columnspan=4, padx=20, pady=10)

        ttk.Button(frame, text="Alugar Caminhão", command=self.rent_truck).grid(row=7, column=0, pady=10)

        ttk.Button(frame, text="Remover Caminhão", command=self.remove_truck).grid(row=7, column=2, pady=10)
        ttk.Button(frame, text="Caminhões Disponíveis", command=self.show_available_trucks).grid(row=8, column=0, pady=10)
        ttk.Button(frame, text="Caminhões Alugados", command=self.show_rented_trucks).grid(row=8, column=1, pady=10)

    def add_truck(self):
        name = self.name_var.get()
        year = self.year_var.get()
        value = self.value_var.get()

        if not name or not year or not value:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        try:
            year = int(year)
            value = float(value)
        except ValueError:
            messagebox.showerror("Erro", "Ano e valor devem ser números válidos.")
            return

        session = get_session()
        new_truck = Truck(name=name, year=year, value=value)
        session.add(new_truck)
        session.commit()
        session.close()
        messagebox.showinfo("Sucesso", "Caminhão adicionado com sucesso!")
        self.clear_fields()
        self.search_trucks()

    def search_trucks(self, *args):
        search_term = self.search_var.get()
        session = get_session()
        trucks = session.query(Truck).filter(or_(Truck.name.ilike(f'%{search_term}%'), Truck.year == search_term)).all()
        self.update_trucks_list(trucks)
        session.close()

    def update_trucks_list(self, trucks):
        self.trucks_listbox.delete(0, tk.END)
        for truck in trucks:
            status = "Disponível" if truck.available else "Alugado"
            self.trucks_listbox.insert(tk.END, f"ID: {truck.id}, Nome: {truck.name}, Ano: {truck.year}, Valor: {truck.value}, Status: {status}")

    def clear_fields(self):
        self.name_var.set("")
        self.year_var.set("")
        self.value_var.set("")

    def rent_truck(self):
        truck_id = simpledialog.askinteger("Alugar Caminhão", "Insira o ID do caminhão a ser alugado:")
        if truck_id is None:
            return

        session = get_session()
        truck = session.query(Truck).filter(Truck.id == truck_id).first()

        if truck is None:
            messagebox.showerror("Erro", "Caminhão não encontrado.")
        elif not truck.available:
            messagebox.showinfo("Informação", "Caminhão já está alugado.")
        else:
            truck.available = False
            session.commit()
            messagebox.showinfo("Sucesso", "Caminhão alugado com sucesso.")
            self.search_trucks()  # Atualiza a lista de caminhões
        session.close()

    def return_truck(self):
        truck_id = simpledialog.askinteger("Devolver Caminhão", "Insira o ID do caminhão a ser devolvido:")
        if truck_id is None:
            return

        session = get_session()
        truck = session.query(Truck).filter(Truck.id == truck_id).first()

        if truck is None:
            messagebox.showerror("Erro", "Caminhão não encontrado.")
        elif truck.available:
            messagebox.showinfo("Informação", "Caminhão já está disponível.")
        else:
            truck.available = True
            session.commit()
            messagebox.showinfo("Sucesso", "Caminhão devolvido com sucesso.")
            self.search_trucks()  # Atualiza a lista de caminhões
        session.close()

    def remove_truck(self):
        truck_id = simpledialog.askinteger("Remover Caminhão", "Insira o ID do caminhão a ser removido:")
        if truck_id is None:
            return

        session = get_session()
        truck = session.query(Truck).filter(Truck.id == truck_id).first()

        if truck is None:
            messagebox.showerror("Erro", "Caminhão não encontrado.")
        else:
            session.delete(truck)
            session.commit()
            messagebox.showinfo("Sucesso", "Caminhão removido com sucesso.")
            self.search_trucks()  # Atualiza a lista de caminhões
        session.close()

    def show_available_trucks(self):
        session = get_session()
        available_trucks = session.query(Truck).filter(Truck.available == True).all()
        self.update_trucks_list(available_trucks)
        session.close()

    def show_rented_trucks(self):
        session = get_session()
        rented_trucks = session.query(Truck).filter(Truck.available == False).all()
        self.update_trucks_list(rented_trucks)
        session.close()

def main():
    root = tk.Tk()
    app = TruckRentalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
