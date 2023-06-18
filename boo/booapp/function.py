def ufile(f):
    with open('static/upload/'+f.name,'wb+') as doc:
        for chunk in f.chunks():
            doc.write(chunk)