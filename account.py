from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.gridlayout import GridLayout

class MojaAplikacja(App):
    def build(self):
        # Tworzenie głównego interfejsu użytkownika
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Dodawanie zdjęcia profilowego
        obraz_profilowy = Image(source="", size_hint=(None, None), size=(100, 100))
        layout.add_widget(obraz_profilowy)

        # Przycisk do wyboru zdjęcia
        przycisk_wybierz_zdjecie = Button(text='Wybierz zdjęcie profilowe')
        przycisk_wybierz_zdjecie.bind(on_press=self.wybierz_zdjecie_profilowe)
        layout.add_widget(przycisk_wybierz_zdjecie)

        # Tworzenie etykiet i pól tekstowych do wprowadzania danych
        etykiety = ['Imię:', 'Nazwisko:', 'Praca:', 'Szkoła podstawowa:', 'Średnia:', 'Wyższa:', 'Miejscowość:', 'Telefon:', 'Mail:', 'Data urodzenia:', 'Status w związku:']
        pola_tekstowe = {}


        for etykieta in etykiety:
            layout.add_widget(Label(text=etykieta))
            pole_tekstowe = TextInput()
            layout.add_widget(pole_tekstowe)
            pola_tekstowe[etykieta] = pole_tekstowe

        # Dodanie przycisku "Zapisz"
        przycisk_zapisz = Button(text='Zapisz')
        przycisk_zapisz.bind(on_press=self.zapisz_dane)
        layout.add_widget(przycisk_zapisz)

          # Dodanie przycisku "Zapisz"
        przycisk_zapisz = Button(text='Nie chcę podawać')
        przycisk_zapisz.bind(on_press=self.zapisz_dane)
        layout.add_widget(przycisk_zapisz)

        return layout

    def wybierz_zdjecie_profilowe(self, instance):
        # Otwieranie okna wyboru pliku i wybieranie zdjęcia profilowego
        file_chooser = FileChooserIconView()
        file_chooser.path = '.'  # Ustawienie domyślnej ścieżki na bieżący katalog
        file_chooser.filters = ['*.jpg', '*.png', '*.jpeg']  # Filtry plików
        file_chooser.bind(on_submit=self.wybrano_zdjecie_profilowe)
        popup = popup(title="Wybierz zdjęcie profilowe!!!!!!!!!", content=file_chooser, size_hint=(None, None), size=(400, 400))
        popup.open()

    def wybrano_zdjecie_profilowe(self, instance, path, filename):
        # Ustawienie wybranego zdjęcia profilowego
        if filename:
            self.obraz_profilowy.source = filename[0]
            self.obraz_profilowy.reload()

    def zapisz_dane(self, instance):
        # Pobieranie danych wprowadzonych przez użytkownika
        dane_uzytkownika = {}
        for etykieta, pole_tekstowe in pola_tekstowe.items():
            dane_uzytkownika[etykieta] = pole_tekstowe.text

        # Wyświetlanie danych użytkownika
        print("Dane użytkownika:")
        for etykieta, wartosc in dane_uzytkownika.items():
            print(f"{etykieta}: {wartosc}")

if __name__ == '__main__':
    MojaAplikacja().run()



