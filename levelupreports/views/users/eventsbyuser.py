import sqlite3
from django.shortcuts import render
from levelupapi.models import Event
from levelupreports.views import Connection

def event_attendees_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    e.time,
                    e.date,
                    e.id as event_id,
                    g.title as game_name,
                    u.id as user_id,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM
                    levelupapi_event e
                JOIN
                    levelupapi_gamerevent eg ON e.id = eg.event_id
                JOIN
                    levelupapi_gamer gr ON eg.gamer_id = gr.id
                JOIN
                    auth_user u ON gr.user_id = u.id
                JOIN
                    levelupapi_game g ON e.game_id = g.id
            """)

            dataset = db_cursor.fetchall()

            # Take the flat data from the database, and build the
            # following data structure for each gamer.
            #
            # {
            #     1: {
            #         "gamer_id": 1,
            #         "full_name": "Molly Ringwald",
            #         "events": [
            #             {
            #                 "id": 5,
            #                 "date": "2020-12-23",
            #                 "time": "19:00",
            #                 "game_name": "Fortress America"
            #             }
            #         ]
            #     }
            # }

            events_by_gamer = {}

            for row in dataset:
                event = Event()
                event.date = row['date']
                event.time = row['time']
                event.game_name = row['game_name']

                uid = row['user_id']

                if uid in events_by_gamer:
                    events_by_gamer[uid]['events'].append(event)

                else:
                    events_by_gamer[uid] = {}
                    events_by_gamer[uid]['id'] = uid
                    events_by_gamer[uid]['full_name'] = row['full_name']
                    events_by_gamer[uid]['events'] = [event]

            list_of_users_with_events = events_by_gamer.values()

            template = 'users/list_with_events.html'
            context = {
                'event_attendees_list': list_of_users_with_events
            }

            return render(request, template, context)
