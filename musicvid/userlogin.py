from django.shortcuts import  render
import pymysql as mysql
from django.contrib import auth
from django.http import JsonResponse
import ast
def  ActionUserCREATEACC(request):
       return render(request,"user/createacc.html",{'msg':''})

def ActionInsertacc(request):
       adminname = request.POST['adminname']
       adminemail=request.POST['adminemail']
       password = request.POST['password']
       cpassword=request.POST['cpassword']
       if(password==cpassword):
         try:
            dbe = mysql.connect(host="127.0.0.1", port=3306,
                                user="root", password='', db="songvideo")
            cmd = dbe.cursor()
            q="insert into userlogin (username,useremail,password)  value('{0}','{1}','{2}')".format(adminname,adminemail,password)
            cmd.execute(q)
            dbe.commit()
            dbe.close()
            return render(request, "user/createacc.html", {'msg': "account created succesfuly"})
         except Exception as e:
               return render(request, "user/createacc.html", {'msg': "try again"})
       else:
           return render(request, "user/createacc.html", {'msg': "try again"})


def ActionUserlogin(request):
    return render(request, "user/userlogin.html", {'msg': ''})

def ActionUSERLogin(request):
    adminname = request.POST['adminname']
    password = request.POST['password']
    try:
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "select *  from userlogin where username='{0}' and password='{1}'".format(adminname, password)
        cmd.execute(q)
        urec = cmd.fetchone()
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()
        q = "select * from subcategory"
        cmd.execute(q)
        srows = cmd.fetchall()

        if (urec):
            request.session['ADMIN_SES'] = urec
            return render(request, "user/usermainpage.html", {'admin': request.session['ADMIN_SES'],'rows':rows,'srows':srows})
        else:
            return render(request, "user/userlogin.html", {'msg': "Invalid AdminId/Password"})
    except Exception as e:
        return render(request, "user/userlogin.html", {'msg': "Server Error"})


def ActionUserMainInterface(request):
 try:
    request.session['ADMIN_SES'] = urec
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
        q = "select * from userlogin"
        cmd.execute(q)
        urows = cmd.fetchall()
        dbe.close()

        return render(request, "user/usermainpage.html", {'rows': rows, 'srows': srows, 'urows':urows})
    except:
        return render(request, "user/usermainpage", {'rows': [], 'srows': [], 'urows':[]})
 except:
   return render(request, "user/userlogin.html", {'msg': "Invalid AdminId/Password"})

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

def ActionUserCategoryPage(request):
   try:

      dbe = mysql.connect(host="127.0.0.1", port=3306,
                          user="root", password='', db="songvideo")
      cmd = dbe.cursor()


      q = "select * from category"
      cmd.execute(q)
      rows = cmd.fetchall()
      q = "select * from songs"
      cmd.execute(q)
      srows = cmd.fetchall()

      q="select * from userlogin"
      cmd.execute(q)
      urows = cmd.fetchall()
      dbe.close()
      return render(request, "user/usercategory.html", {'rows': rows,'srows':srows,'urows':urows})
   except:
      return render(request, "user/usercategory.html", {'rows': [],'srows':[],'urows':[]})

def ActionUserPlaylistPage(request):
    try:
        q = "select * from category"
        rows =FetchAllRecord(q)
        q="select * from subcategory"
        srows=FetchAllRecord(q)
        return render(request, "user/userplaylist.html", {'rows': rows,'srows':srows})
    except:
        return render(request, "user/userplaylist.html", {'rows': [],'srows':[]})

def ActionUserArtistPage(request):
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
        return render(request, "user/userartist.html", {'rows': rows,'scid':scid})
    except:
        return render(request, "user/userartist.html", {'rows': [],'scid':scid})

def ActionUserSubCategoryPage(request):
    try:
        cid=request.GET["cid"]
        q="select * from subcategory where categoryid={0}".format(cid)
        rows=FetchAllRecord(q)
        q = "select * from songs"
        srows = FetchAllRecord(q)

        return render(request, "user/usersubcategory.html", {'rows': rows,'srows':srows})

    except:
        return render(request, "user/usersubcategory.html", {'rows': [],'srows':[]})

def ActionUserSearchSongPage(request):
    try:

        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "select * from songs"
        cmd.execute(q)
        rows = cmd.fetchall()

        dbe.close()
        return render(request, "user/usersearchsong.html", {'rows': rows})
    except:
        return render(request, "user/usersearchsong.html", {'rows': []})

def ActionUserSearchSongJson(request):
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

def ActionUserPlaySong(request):
    try:
        sg= request.GET["sg"]
        print("xxxxxx",sg)
        sg=sg.split(",")
        print(sg)
        q = "select *  from songs where songsid={0}".format(sg[0])
        print(q)
        rows = FetchAllRecord(q)
        print(rows)
        return render(request, "user/userplaysong.html", {'row': rows[0]})
    except Exception as e:
        print("Error",e)
        return render(request, "user/userplaysong.html", {'row': []})


def ActionUserContact(request):
    try:
        return render(request, "user/usercontact.html", {'msg':''})
    except:
        return render(request, "user/usercontact.html", {'msg':''})

def ActionUserContactmessage(request):
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

        return render(request, "user/usercontact.html", {'msg':'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "user/usercontact.html", {'msg': 'Fail to Submit Record'})
def ActionUserblog(request):
    try:
        q = "select * from category"
        rows =FetchAllRecord(q)
        q="select * from subcategory"
        srows=FetchAllRecord(q)
        return render(request, "user/userblog.html", {'rows': rows,'srows':srows})
    except:
        return render(request, "user/userblog.html", {'rows': [],'srows':[]})


def ActionLogoutUser(request):
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
        auth.logout(request)
        return render(request, "soulmusic/index.html", {'msg': '','rows': rows, 'srows': srows})


    except:
        return render(request, "soulmusic/index.html", {'rows': [], 'srows': []})
