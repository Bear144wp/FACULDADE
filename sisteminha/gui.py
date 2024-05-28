import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
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

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True, fill=tk.BOTH)

        title = ttk.Label(frame, text="Sistema de Aluguel de Caminhões", font=("Arial", 24, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=20)

        ttk.Label(frame, text="Nome").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.name_var, width=30).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ano").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.year_var = tk.IntVar()
        ttk.Entry(frame, textvariable=self.year_var, width=30).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Valor").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.value_var = tk.DoubleVar()
        ttk.Entry(frame, textvariable=self.value_var, width=30).grid(row=3, column=1, padx=5, pady=5)

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="Adicionar Caminhão", command=self.add_truck).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="Remover Caminhão", command=self.remove_truck).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Alugar Caminhão", command=self.rent_truck).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(button_frame, text="Devolver Caminhão", command=self.return_truck).grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(button_frame, text="Ver Caminhões Disponíveis", command=self.show_available_trucks).grid(row=0, column=4, padx=5, pady=5)

    def add_truck(self):
        session = get_session()
        new_truck = Truck(name=self.name_var.get(), year=self.year_var.get(), value=self.value_var.get())
        session.add(new_truck)
        session.commit()
        session.close()
        messagebox.showinfo("Sucesso", "Caminhão adicionado com sucesso!")

    def remove_truck(self):
        truck_id = simpledialog.askinteger("Remover Caminhão", "Digite o ID do caminhão a ser removido:")
        if truck_id:
            session = get_session()
            truck = session.query(Truck).filter_by(id=truck_id).first()
            if truck:
                session.delete(truck)
                session.commit()
                session.close()
                messagebox.showinfo("Sucesso", "Caminhão removido com sucesso!")
            else:
                session.close()
                messagebox.showerror("Erro", "Caminhão não encontrado.")

    def rent_truck(self):
        truck_id = simpledialog.askinteger("Alugar Caminhão", "Digite o ID do caminhão a ser alugado:")
        if truck_id:
            session = get_session()
            truck = session.query(Truck).filter_by(id=truck_id).first()
            if truck and truck.available:
                truck.available = False
                session.commit()
                session.close()
                messagebox.showinfo("Sucesso", "Caminhão alugado com sucesso!")
            elif truck:
                session.close()
                messagebox.showerror("Erro", "Caminhão já está alugado.")
            else:
                session.close()
                messagebox.showerror("Erro", "Caminhão não encontrado.")

    def return_truck(self):
        truck_id = simpledialog.askinteger("Devolver Caminhão", "Digite o ID do caminhão a ser devolvido:")
        if truck_id:
            session = get_session()
            truck = session.query(Truck).filter_by(id=truck_id).first()
            if truck and not truck.available:
                truck.available = True
                session.commit()
                session.close()
                messagebox.showinfo("Sucesso", "Caminhão devolvido com sucesso!")
            elif truck:
                session.close()
                messagebox.showerror("Erro", "Caminhão já está disponível.")
            else:
                session.close()
                messagebox.showerror("Erro", "Caminhão não encontrado.")

    def show_available_trucks(self):
        session = get_session()
        trucks = session.query(Truck).filter_by(available=True).all()
        available_trucks = "\n".join([f"ID: {truck.id}, Nome: {truck.name}, Ano: {truck.year}, Valor: {truck.value}" for truck in trucks])
        session.close()
        messagebox.showinfo("Caminhões Disponíveis", available_trucks)

def main():
    root = tk.Tk()
    app = TruckRentalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
