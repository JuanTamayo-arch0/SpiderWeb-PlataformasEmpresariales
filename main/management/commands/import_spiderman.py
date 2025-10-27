import os
import pandas as pd
from django.core.management.base import BaseCommand
from main.models import SpidermanVariant

class Command(BaseCommand):
    help = 'Importa variantes de Spider-Man desde un archivo Excel'

    def handle(self, *args, **kwargs):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_path = os.path.join(BASE_DIR, 'data', 'Spider-Man_Variants.xlsx')

        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
            SpidermanVariant.objects.create(
                imagen=row['Imagen'],
                nombre=row['Nombre del personaje'],
                datos=row['Datos'],
                descripcion=row['Descripción']
            )

        self.stdout.write(self.style.SUCCESS('Datos importados exitosamente.'))
