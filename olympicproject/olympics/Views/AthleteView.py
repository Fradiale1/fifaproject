import datetime
from django.http import JsonResponse
from django.views import View
from olympics.repository.AthleteRepository import AthleteRepository
from django_request_mapping import request_mapping

@request_mapping("/athletes")
class AthleteView(View):

    def __init__(self):
        super().__init__()
        self.athlete_repository: AthleteRepository = AthleteRepository(
            db_url='mongodb://localhost:27017/',  # Inserisci l'URL del tuo database MongoDB
            db_name='Olympic'  # Inserisci il nome del tuo database MongoDB
        )

    @request_mapping("/getAll", method="get")
    def get_all_athletes(self, request):
        athletes = self.athlete_repository.get_all_athletes()
        #year = int(datetime.date.today().strftime("%Y"))
        
        data = []
        for athlete in athletes:
            #athlet_age = athlete.get('athlete_year_birth', '')
            #if(athlet_age != ''):
            #    athlet_age = int(year) - athlet_age

            athlete_data = {
                'id': str(athlete['_id']),  # Converti ObjectId in stringa per JSON
                'name': athlete.get('athlete_full_name', ''),  # Utilizza get per evitare KeyError
                'prime_olimpiadi': athlete.get('first_game', ''),  # Utilizza get per evitare KeyError
                'anno_nascita': athlete.get('athlete_year_birth', '')  # Utilizza get per evitare KeyError
            }
            data.append(athlete_data)

        return JsonResponse(data, safe=False)

    @request_mapping("/getById/<str:athlete_id>", method="get") #@get("/{athlete_id}")
    def get_athlete_by_id(self, request, athlete_id):
        athlete = self.athlete_repository.get_athlete_by_id(athlete_id)
        #data = {"id": str(athlete._id), "name": athlete.name, "sport": athlete.sport, "age": athlete.age}
        data = {
                'id': str(athlete['_id']),  # Converti ObjectId in stringa per JSON
                'name': athlete.get('athlete_full_name', ''),  # Utilizza get per evitare KeyError
                'prime_olimpiadi': athlete.get('first_game', ''),  # Utilizza get per evitare KeyError
                'anno_nascita': athlete.get('athlete_year_birth', '')  # Utilizza get per evitare KeyError
            }
        return JsonResponse(data)
    
    @request_mapping("/create", method="post")
    def create_athlete(self, request):
        data = request.POST
        athlete = self.athlete_repository.create_athlete(data.get('name'), data.get('sport'), data.get('age'))
        return JsonResponse({"id": str(athlete._id), "name": athlete.name, "sport": athlete.sport, "age": athlete.age})

    @request_mapping("/update/<str:athlete_id>", method="post")
    def update_athlete(self, request, athlete_id):
        data = request.POST
        athlete = self.athlete_repository.update_athlete(athlete_id, data.get('name'), data.get('sport'), data.get('age'))
        return JsonResponse({"id": str(athlete._id), "name": athlete.name, "sport": athlete.sport, "age": athlete.age})

    @request_mapping("/delete/<str:athlete_id>", method="post")
    def delete_athlete(self, request, athlete_id):
        self.athlete_repository.delete_athlete(athlete_id)
        return JsonResponse({"message": "Atleta Eliminato"})