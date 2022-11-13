from django.shortcuts import  render
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import pymysql as mysql
@xframe_options_exempt
def ActionSongsInterface(request):
  try:
    rec = request.session['ADMIN_SES']
    return render(request, "songsinterface.html", {'msg': ''})
  except:
      return render(request, "NewAdminLogin.html", {'msg': ''})


@xframe_options_exempt
def ActionSubmitSongs(request):
    categoryid = request.POST['cid']
    scid=request.POST['subid']
    stitle = request.POST['stitle']
    releaseyear = request.POST['releaseyear']
    slyrics = request.FILES['slyrics']
    status = request.POST['status']
    type = request.POST['type']
    ssinger= request.POST['ssinger']
    sdirector = request.POST['sdirector']
    scompany = request.POST['scompany']
    sposter = request.FILES['sposter']

    try:
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()

        q = "insert into songs (subcategoryid,title,releaseyear,lyrics,status,type,singers,director,musiccompany,poster,categoryid) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}',{10})".format(scid,stitle,releaseyear, slyrics,status,type,ssinger,sdirector,scompany,sposter.name,categoryid)

        cmd.execute(q)
        dbe.commit()
        dbe.close()
        # upload file

        a = open("d:/musicvid/asset/" + sposter.name, "wb")
        f = open("d:/musicvid/asset/" + slyrics.name, "wb")

        for chunk in sposter.chunks():

            a.write(chunk)
        a.close()
        for chunk in slyrics.chunks():
            f.write(chunk)
        f.close


        return render(request, "Songsinterface.html", {'msg': 'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "Songsinterface.html", {'msg': 'Fail to Submit Record'})

@xframe_options_exempt
def ActionSongsDisplayAll(request):
   try:
    rec = request.session['ADMIN_SES']
    try:
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        #q = "select * from songs"
        q = "select S.*, (select C.categoryname from category C where C.categoryid=S.categoryid) as categoryname  from songs S"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return render(request, "songsdisplayall.html", {'rows': rows})
    except Exception as e:
        print(e)
        return render(request, "songsdisplayall.html", {'rows': []})
   except:
       return render(request, "NewAdminLogin.html", {'msg': ''})

@xframe_options_exempt
def ActionSongsDisplayByid(request):
   try:
    rec = request.session['ADMIN_SES']
    try:
        sgcid = request.GET['sgcid']
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "select S.*, (select C.categoryname from category C where C.categoryid=S.categoryid) as categoryname  from songs S where S.songsid={0}".format(sgcid)

        cmd.execute(q)
        row = cmd.fetchone()
        dbe.close()
        return render(request, "songsdisplaybyid.html", {'row': row})
    except Exception as e:
        print(e)
        return render(request, "songsdisplaybyid.html", {'row': []})
   except:
       return render(request, "NewAdminLogin.html", {'msg': ''})
@xframe_options_exempt
def ActionSongsEditDeleteSubmit(request):
    sgcid=request.POST['sgcid']
    scid=request.POST['subid']


    stitle = request.POST['stitle']
    releaseyear = request.POST['releaseyear']
    status = request.POST['status']
    type = request.POST['type']
    ssinger = request.POST['ssinger']
    sdirector = request.POST['sdirector']
    scompany = request.POST['scompany']
    cid=request.POST['cid']

    btn = request.POST['btn']

    try:
        if (btn == "Edit"):
            dbe = mysql.connect(host="127.0.0.1", port=3306,
                                user="root", password='', db="songvideo")
            cmd = dbe.cursor()
            q = "update songs set title='{0}',releaseyear='{1}',status='{2}',type='{3}',singers='{4}',director='{5}',musiccompany='{6}' where songsid='{7}'".format(stitle,releaseyear,status,type,ssinger,sdirector,scompany,sgcid)

            cmd.execute(q)
            dbe.commit()
            dbe.close()
            return ActionSongsDisplayAll(request)


        elif (btn == "Delete"):
            dbe = mysql.connect(host="127.0.0.1", port=3306,
                                user="root", password='', db="songvideo")
            cmd = dbe.cursor()
            q = "delete from songs where songsid='{0}'".format(sgcid)
            cmd.execute(q)
            dbe.commit()
            dbe.close()
            return ActionSongsDisplayAll(request)
    except Exception as e:
        return ActionSongsDisplayAll(request)
@xframe_options_exempt
def ActionEditSongsPicture(request):
    sgcid = request.POST['sgcid']
    sposter = request.FILES['sposter']
    slyrics=request.FILES['slyrics']
    try:
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "update songs  set poster='{0}',lyrics='{1}' where songsid='{2}'".format(sposter.name,slyrics.name,sgcid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        # upload file

        a = open("d:/musicvid/asset/" + sposter.name, "wb")
        f = open("d:/musicvid/asset/" + slyrics.name, "wb")
        for chunk in sposter.chunks():

            a.write(chunk)
        a.close()
        for chunk in slyrics.chunks():
            f.write(chunk)
        f.close()    
        return ActionSongsDisplayAll(request)

    except Exception as e:
        print(e)
        return ActionSongsDisplayAll(request)

#def ActionDisplaySubCategoryJson(request):
 #  try:
  #  rec = request.session['ADMIN_SES']
   # try:
    #    cid = request.GET['cid']


#        dbe = mysql.connect(host="127.0.0.1", port=3306,
 #                           user="root", password='', db="songvideo")
  #      cmd = dbe.cursor()
   #     q = "select * from subcategory where categoryid={0}".format(cid)
    #    cmd.execute(q)
     #   rows = cmd.fetchall()
      #  dbe.close()


       # return JsonResponse(rows,safe=False)
    #except Exception as e:
     #   print(e)
      #  return  JsonResponse({})
   #except:
    #   return render(request, "NewAdminLogin.html", {'msg': ''})

def ActionDisplaySubCategoryJson(request):
    try:
       rec = request.session['ADMIN_SES']
       try:
           cid = request.GET['cid']
           dbe = mysql.connect(host="127.0.0.1", port=3306,
                                   user="root", password='', db="songvideo")
           cmd = dbe.cursor()
           q = "select * from subcategory where categoryid={0}".format(cid)
           cmd.execute(q)
           rows = cmd.fetchall()
           dbe.close()
           return JsonResponse(rows, safe=False)
       except Exception as e:
           print(e)
           return JsonResponse({})
    except:
           return render(request, "NewAdminLogin.html", {'msg': ''})


@xframe_options_exempt
def ActionShowAllSongs(request):
    try:
       rec = request.session['ADMIN_SES']
       try:
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q="select * from songs"
              cmd.execute(q)
              srows=cmd.fetchall()
              dbe.close()
              return render(request, "showsongs.html",{'srows':srows})
       except Exception as e:
              print(e)
              return render(request, "showsongs.html",{'srows':[]})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})
