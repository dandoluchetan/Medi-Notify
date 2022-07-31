from unesco.models import Category,State,Iso,Region,Site
import csv
def run():
    file_csv=open('~/django_projects/batch/unesco/whc-sites-2018-clean.csv')
    reader=csv.reader(file_csv)
    next(reader)

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        C,created=Category.objects.get_or_create(name=row[7])
        S,created=State.objects.get_or_create(name=row[8])
        R,created=Region.objects.get_or_create(name=row[9])
        I,created=Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None
        try:
            lon = int(row[4])
        except:
            lon = None
        try:
            lat = int(row[5])
        except:
            lat = None
        try:
            ah = int(row[6])
        except:
            ah = None
            
        site1=Site(name=row[0],description=row[1],justification=row[2],year=y,longitude=lon,latitude=lat,area_hectares=ah,category=C,state=S,region=R,iso=I)
        site1.save()
    

