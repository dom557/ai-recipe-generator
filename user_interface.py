import json
import os
import tkinter as tk
from tkinter import messagebox, ttk
import recipe_generator

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('AI Recipe Generator')
        self.root.configure(bg='#1E1E1E')

        # Set primary and secondary colors
        primary_color = '#1E1E1E'
        button_color = '#FFA500'  # Orange color for buttons
        text_color = '#FFFFFF'  # White color for text

        # Set window width and height
        window_width = 600
        window_height = 600

        # Calculate center position for window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2.3) - (window_height / 2))

        # Set window size and position
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')

        # Create UI elements
        self.generated_recipe_label = tk.Label(self.root, text='Generated Recipe:', font=('Arial', 16), fg=text_color, bg=primary_color)
        self.generated_recipe_label.pack(pady=10)

        self.generated_recipe_text = tk.Text(self.root, width=60, height=10, font=('Arial', 12), fg=primary_color, bg=button_color, bd=0)
        self.generated_recipe_text.pack(pady=10)

        self.generate_button = tk.Button(self.root, text='Generate Recipe', command=self.generate_recipe, font=('Arial', 12), bg=button_color, fg=text_color)
        self.generate_button.pack(pady=10)

        self.suggest_button = tk.Button(self.root, text='Suggest Recipe', command=self.suggest_recipe, font=('Arial', 12), bg=button_color, fg=text_color)
        self.suggest_button.pack(pady=10)

        self.return_button = tk.Button(self.root, text='Return', command=self.return_to_main, font=('Arial', 12), bg=button_color, fg=text_color)
        self.return_button.pack(pady=10)

        # Initialize style
        self.style = ttk.Style()
        self.style.configure('TEntry', background='white', foreground='#7fbffc', font=('Arial', 12))
        self.style.configure('TText', background='white', foreground='#7fbffc', font=('Arial', 12))
        # self.style.configure('TButton', font=('Arial', 12), background='#FFA500')

    def run(self):
        self.root.mainloop()

    def generate_recipe(self):
        try:
            generator = recipe_generator.RecipeGenerator()
            recipe_data = generator.generate_recipe()

            recipe_name = recipe_data['name']
            origin = recipe_data['origin']
            ingredients = "\n".join(recipe_data['ingredients'])
            instructions = "\n".join(recipe_data['instructions'])

            formatted_recipe = f"Recipe Name: {recipe_name}\nOrigin: {origin}\n\nIngredients:\n{ingredients}\n\nInstructions:\n{instructions}"

            self.generated_recipe_text.delete('1.0', tk.END)
            self.generated_recipe_text.insert(tk.END, formatted_recipe)
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def suggest_recipe(self):
        suggest_window = tk.Toplevel(self.root)
        suggest_window.title('Suggest Recipe')
        suggest_window.geometry('400x500')
        suggest_window.configure(bg='#1E1E1E', pady=10)

        recipe_name_label = ttk.Label(suggest_window, text='Recipe Name:', style='TLabel')
        recipe_name_label.pack(pady=10)

        recipe_name_entry = ttk.Entry(suggest_window, width=30)
        recipe_name_entry.pack(pady=5)

        ingredients_label = ttk.Label(suggest_window, text='Ingredients:', style='TLabel')
        ingredients_label.pack(pady=10)

        ingredients_entry = tk.Text(suggest_window, height=5, width=30)
        ingredients_entry.pack(pady=5)

        instructions_label = ttk.Label(suggest_window, text='Instructions:', style='TLabel')
        instructions_label.pack(pady=10)

        instructions_entry = tk.Text(suggest_window, height=10, width=30)
        instructions_entry.pack(pady=5)

        confirm_button = tk.Button(suggest_window, text='Confirm', command=lambda: self.confirm_suggested_recipe(
            suggest_window, recipe_name_entry.get(), ingredients_entry.get('1.0', 'end-1c'),
            instructions_entry.get('1.0', 'end-1c')
        ), bg="#FFA500")
        confirm_button.pack(pady=10)

    def confirm_suggested_recipe(self, window, recipe_name, ingredients, instructions):
        suggested_recipe = {
            'recipe_name': recipe_name,
            'ingredients': ingredients,
            'instructions': instructions
        }
        try:
            # Read the contents of the JSON file
            with open ('recipes.json', 'r') as file:
             data = json.load (file)

            # Add the suggested recipe to the existing recipes
            data ['recipes'].append (suggested_recipe)

            if recipe_name == "" or ingredients == "" or instructions == "":
                messagebox.showwarning("Warning", "You haven't filled everything")
            elif recipe_name and ingredients and instructions:
    # Write the updated data back to the JSON file
                with open('recipes.json', 'w') as file:
                    json.dump(data, file)
                    messagebox.showinfo('Suggested Recipe', 'Recipe added successfully!')
                    window.destroy()

            

        except Exception as e:
            messagebox.showerror('Error', str(e))

    def return_to_main(self):
        self.generated_recipe_text.delete('1.0', tk.END)

if __name__ == '__main__':
    ui = UserInterface()
    ui.run()
