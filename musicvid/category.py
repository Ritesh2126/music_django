from django.shortcuts import  render
from django.views.decorators.clickjacking import xframe_options_exempt
import pymysql as mysql
from django.http import JsonResponse


@xframe_options_exempt

def  ActionCategoryInterface(request):
    try:
       rec=request.session['ADMIN_SES']
       return render(request,"categoryinterface.html",{'msg':''})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})
@xframe_options_exempt
def ActionSubmitCategory(request):
       cname=request.POST['cname']
       cdes = request.POST['cdes']
       file= request.FILES['cicon']

       try:
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q="insert into category (categoryname,categorydescription,categoryicon)  value('{0}','{1}','{2}')".format(cname,cdes,file.name)
              cmd.execute(q)
              dbe.commit()
              dbe.close()
              # upload file
              f = open("d:/musicvid/asset/" + file.name, "wb")
              for chunk in file.chunks():
                     f.write(chunk)
              f.close()


              return render(request,"CategoryInterface.html",{'msg':'Record Submitted'})
       except Exception as e:
              print(e)
              return render(request, "CategoryInterface.html", {'msg': 'Fail to Submit Record'})

@xframe_options_exempt
def ActionDisplayAll(request):
    try:
       rec = request.session['ADMIN_SES']
       try:
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q="select * from category"
              cmd.execute(q)
              rows=cmd.fetchall()
              dbe.close()
              return render(request, "categorydisplayall.html",{'rows':rows})
       except Exception as e:
              print(e)
              return render(request, "categorydisplayall.html",{'rows':[]})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})

@xframe_options_exempt
def ActionDisplayByid(request):
    try:
       rec = request.session['ADMIN_SES']
       try:
              cid=request.GET['cid']
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q="select *  from category where categoryid={0}".format(cid)
              cmd.execute(q)
              row=cmd.fetchone()
              dbe.close()
              return render(request, "categorydisplaybyid.html",{'row':row})
       except Exception as e:
              print(e)
              return render(request, "categorydisplaybyid.html",{'row':[]})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})



@xframe_options_exempt
def ActionCategoryEditDeleteSubmit(request):
       cid=request.POST['cid']
       cname=request.POST['cname']
       cdes = request.POST['cdes']

       btn=request.POST['btn']

       try:
        if(btn=="Edit"):
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q="update category set categoryname='{0}',categorydescription='{1}' where categoryid='{2}'".format(cname,cdes,cid)
              cmd.execute(q)
              dbe.commit()
              dbe.close()
              return ActionDisplayAll(request)


        elif(btn=="Delete"):
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q = "delete from category where categoryid='{0}'".format(cid)
              cmd.execute(q)
              dbe.commit()
              dbe.close()
              return ActionDisplayAll(request)
       except Exception as e:
              return ActionDisplayAll(request)
@xframe_options_exempt
def ActionEditCategoryPicture(request):
       cid = request.POST['cid']
       file = request.FILES['cicon']

       try:
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q = "update category  set categoryicon='{0}' where categoryid={1}".format(file.name,cid)
              cmd.execute(q)
              dbe.commit()
              dbe.close()
              # upload file
              f = open("d:/musicvid/asset/" + file.name, "wb")
              for chunk in file.chunks():
                     f.write(chunk)
              f.close()
              return ActionDisplayAll(request)

       except Exception as e:
              print(e)
              return ActionDisplayAll(request)


def ActionDisplayJson(request):
  try:
    rec = request.session['ADMIN_SES']
    try:
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()

        return JsonResponse(rows,safe=False)
    except Exception as e:
        print(e)
        return  JsonResponse({})
  except:
      return render(request, "NewAdminLogin.html", {'msg': ''})

@xframe_options_exempt
def Actionmessagedisplay(request):
    try:
       rec = request.session['ADMIN_SES']
       try:
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q="select * from message"
              cmd.execute(q)
              rows=cmd.fetchall()
              dbe.close()
              return render(request, "messagedisplayall.html",{'rows':rows})
       except Exception as e:
              print(e)
              return render(request, "messagedisplayall.html",{'rows':[]})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})
@xframe_options_exempt
def ActionShowCategory(request):
    try:
       rec = request.session['ADMIN_SES']
       try:
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q="select * from category"
              cmd.execute(q)
              rows=cmd.fetchall()
              dbe.close()
              return render(request, "showcategory.html",{'rows':rows})
       except Exception as e:
              print(e)
              return render(request, "showcategory.html",{'rows':[]})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})
@xframe_options_exempt
def ActionShowSubCategory(request):
    cid = request.GET['cid']
    try:

       rec = request.session['ADMIN_SES']

       try:
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q="select * from category"
              cmd.execute(q)
              rows=cmd.fetchall()
              q = "select * from subcategory where categoryid='{0}'".format(cid)
              cmd.execute(q)
              srows = cmd.fetchall()
              dbe.close()
              return render(request, "showsubcategory.html",{'rows':rows,'srows':srows})
       except Exception as e:
              print(e)
              return render(request, "showsubcategory.html",{'rows':[],'srows':[]})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})


@xframe_options_exempt
def ActionShowSongs(request):
    scid = request.GET['scid']
    try:

        rec = request.session['ADMIN_SES']

        try:
            dbe = mysql.connect(host="127.0.0.1", port=3306,
                                user="root", password='', db="songvideo")
            cmd = dbe.cursor()
            q = "select * from subcategory"
            cmd.execute(q)
            rows = cmd.fetchall()
            q = "select * from songs where subcategoryid='{0}'".format(scid)
            cmd.execute(q)
            srows = cmd.fetchall()
            dbe.close()
            return render(request, "showsongs.html", {'rows': rows, 'srows': srows})
        except Exception as e:
            print(e)
            return render(request, "showsongs.html", {'rows': [], 'srows': []})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})