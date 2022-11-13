
from django.shortcuts import  render
import pymysql as mysql
from django.http import JsonResponse
import ast



def  ActionMainInterface(request):
              try:
                     dbe = mysql.connect(host="127.0.0.1", port=3306,
                                         user="root", password='', db="songvideo")
                     cmd = dbe.cursor()
                     q = "select * from category"
                     cmd.execute(q)
                     rows = cmd.fetchall()
                     q = "select * from subcategory"
                     cmd.execute(q)
                     srows = cmd.fetchall()
                     dbe.close()

                     return render(request,"soulmusic/index.html", {'rows': rows,'srows':srows})
              except:
                     return render(request, "soulmusic/index.html", {'rows': [],'srows':[]})

def FetchAllRecord(q):
  try:
     dbe = mysql.connect(host="127.0.0.1", port=3306,
                         user="root", password='', db="songvideo")
     cmd = dbe.cursor()
     cmd.execute(q)
     rows = cmd.fetchall()
     dbe.close()
     return rows
  except Exception as e:
       print(e)
       return []

def ActionCategoryPage(request):
    try:
        q="select * from category"
        rows=FetchAllRecord(q)
        q="select * from songs"
        srows=FetchAllRecord(q)

        return render(request, "soulmusic/category.html", {'rows': rows,'srows':srows})
    except:
        return render(request, "soulmusic/category.html", {'rows': [],'srows':[]})



def ActionPlaylistPage(request):
    try:
        q = "select * from category"
        rows =FetchAllRecord(q)
        q="select * from subcategory"
        srows=FetchAllRecord(q)
        return render(request, "soulmusic/playlist.html", {'rows': rows,'srows':srows})
    except:
        return render(request, "soulmusic/playlist.html", {'rows': [],'srows':[]})

def ActionArtistPage(request):
    try:

        scid=request.GET['scid']

        print(scid)
        scid=ast.literal_eval(scid)
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "select * from songs where subcategoryid={0}".format(scid[0])
        cmd.execute(q)
        rows = cmd.fetchall()


        dbe.close()
        return render(request, "soulmusic/artist.html", {'rows': rows,'scid':scid})
    except:
        return render(request, "soulmusic/artist.html", {'rows': [],'scid':scid})

def ActionSubCategoryPage(request):
    try:
        cid=request.GET["cid"]
        q="select * from subcategory where categoryid={0}".format(cid)
        rows=FetchAllRecord(q)
        q = "select * from songs"
        srows = FetchAllRecord(q)

        return render(request, "soulmusic/subcategory.html", {'rows': rows,'srows':srows})

    except:
        return render(request, "soulmusic/subcategory.html", {'rows': [],'srows':[]})

def ActionSearchSongPage(request):
    try:

        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "select * from songs"
        cmd.execute(q)
        rows = cmd.fetchall()

        dbe.close()
        return render(request, "soulmusic/searchsong.html", {'rows': rows})
    except:
        return render(request, "soulmusic/searchsong.html", {'rows': []})

def ActionSearchSongJson(request):
    try:
        pat=request.GET['pat']

        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "select * from songs where title like '%{0}%'".format(pat)
        cmd.execute(q)
        rows = cmd.fetchall()

        dbe.close()
        return JsonResponse(rows,safe=False)
    except:
        return JsonResponse(rows,safe=False)

def ActionPlaySong(request):
    try:
        sg= request.GET["sg"]
        print("xxxxxx",sg)
        sg=sg.split(",")
        print(sg)
        q = "select *  from songs where songsid={0}".format(sg[0])
        print(q)
        rows = FetchAllRecord(q)
        print(rows)
        return render(request, "soulmusic/playsong.html", {'row': rows[0]})
    except Exception as e:
        print("Error",e)
        return render(request, "soulmusic/playsong.html", {'row': []})


def ActionContact(request):
    try:
        return render(request, "soulmusic/contact.html", {'msg':''})
    except:
        return render(request, "soulmusic/contact.html", {'msg':''})

def ActionContactmessage(request):
    personname = request.GET['personname']
    email = request.GET['email']
    subject= request.GET['subject']
    message=request.GET['message']

    try:
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "insert into message (personname,email,subject,message)  value('{0}','{1}','{2}','{3}')".format(personname, email,subject,message)
        cmd.execute(q)
        dbe.commit()
        dbe.close()

        return render(request, "soulmusic/contact.html", {'msg':'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "soulmusic/contact.html", {'msg': 'Fail to Submit Record'})
def Actionblog(request):
    try:
        q = "select * from category"
        rows =FetchAllRecord(q)
        q="select * from subcategory"
        srows=FetchAllRecord(q)
        return render(request, "soulmusic/blog.html", {'rows': rows,'srows':srows})
    except:
        return render(request, "soulmusic/blog.html", {'rows': [],'srows':[]})