import reflex as rx

#Index

index_title= "LeoCoves | Link Bio - Mi portafolio personal"
index_description= "Link Bio es un sitio web que permite conocerme mas y ver mis trabajos y redes sociales."

index_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:site_name", "content": index_title},
    {"name": "og:title", "content": index_description},
    {"name": "og:description", "content": "@leocovess"}
]



#Cursos

courses_title= "LeoCoves | Link Bio - Cursos"
courses_description= "Esto es de prueba"

courses_meta = [
    {"name": "og:site_name", "content": courses_title},
    {"name": "og:title", "content": courses_description},
    {"name": "og:description", "content": "@leocovess"}
]

courses_meta.extend(index_meta)



