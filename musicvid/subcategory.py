from django.shortcuts import  render
from django.views.decorators.clickjacking import xframe_options_exempt

import pymysql as mysql


@xframe_options_exempt
def ActionSubCategoryInterface(request):
    try:
       rec = request.session['ADMIN_SES']
       return render(request, "subcategoryinterface.html", {'msg': ''})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})

@xframe_options_exempt
def ActionSubmitSubCategory(request):
    cid=request.POST['cid']
    scname = request.POST['scname']
    scdes = request.POST['scdes']
    sfile = request.FILES['scicon']
    print(cid,scname,scdes,sfile)
    try:
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "insert into subcategory (categoryid,subcategoryname,subcategorydescription,subcategoryicon) values('{0}','{1}','{2}','{3}')".format(cid,scname, scdes, sfile.name)

        cmd.execute(q)
        dbe.commit()
        dbe.close()
        # upload file
        f = open("d:/musicvid/asset/" + sfile.name, "wb")
        for chunk in sfile.chunks():
            f.write(chunk)
        f.close()


        return render(request, "SubCategoryInterface.html", {'msg': 'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "SubCategoryInterface.html", {'msg': 'Fail to Submit Record'})


@xframe_options_exempt
def ActionSubCategoryDisplayAll(request):
    try:
       rec = request.session['ADMIN_SES']
       try:
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q = "select S.*, (select C.categoryname from category C where C.categoryid=S.categoryid) as categoryname  from subcategory S"

              cmd.execute(q)
              rows=cmd.fetchall()
              dbe.close()
              return render(request, "subcategorydisplayall.html",{'rows':rows})
       except Exception as e:
              print(e)
              return render(request, "subcategorydisplayall.html",{'rows':[]})
    except:
        return render(request, "NewAdminLogin.html", {'msg': ''})
@xframe_options_exempt
def ActionSubCategoryDisplayByid(request):
  try:
    rec = request.session['ADMIN_SES']
    try:
        scid = request.GET['scid']
        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "select S.*, (select C.categoryname from category C where C.categoryid=S.categoryid) as categoryname  from subcategory S where S.subcategoryid={0}".format(scid)

        cmd.execute(q)
        row = cmd.fetchone()
        dbe.close()
        return render(request, "subcategorydisplaybyid.html", {'row': row})
    except Exception as e:
        print(e)
        return render(request, "subcategorydisplaybyid.html", {'row': []})
  except:
      return render(request, "NewAdminLogin.html", {'msg': ''})
@xframe_options_exempt
def ActionSubCategoryEditDeleteSubmit(request):
    scid = request.POST['scid']
    scname = request.POST['scname']
    scdes = request.POST['scdes']

    btn = request.POST['btn']

    try:
        if (btn == "Edit"):
            dbe = mysql.connect(host="127.0.0.1", port=3306,
                                user="root", password='', db="songvideo")
            cmd = dbe.cursor()
            q = "update subcategory set subcategoryname='{0}',subcategorydescription='{1}' where subcategoryid='{2}'".format(scname,scdes,scid)
            cmd.execute(q)
            dbe.commit()
            dbe.close()
            return ActionSubCategoryDisplayAll(request)


        elif (btn == "Delete"):
            dbe = mysql.connect(host="127.0.0.1", port=3306,
                                user="root", password='', db="songvideo")
            cmd = dbe.cursor()
            q = "delete from subcategory where subcategoryid='{0}'".format(scid)
            cmd.execute(q)
            dbe.commit()
            dbe.close()
            return ActionSubCategoryDisplayAll(request)
    except Exception as e:
        return ActionSubCategoryDisplayAll(request)
@xframe_options_exempt
def ActionEditSubCategoryPicture(request):
    scid = request.POST['scid']
    sfile = request.FILES['scicon']

    try:

        dbe = mysql.connect(host="127.0.0.1", port=3306,
                            user="root", password='', db="songvideo")
        cmd = dbe.cursor()
        q = "update subcategory  set subcategoryicon='{0}' where subcategoryid='{1}'".format(sfile.name, scid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        # upload file
        f = open("d:/musicvid/asset/" + sfile.name, "wb")
        for chunk in sfile.chunks():
            f.write(chunk)
        f.close()
        return ActionSubCategoryDisplayAll(request)

    except Exception as e:
        print(e)
        return ActionSubCategoryDisplayAll(request)

@xframe_options_exempt
def ActionShowSubCategory(request):
    try:
       rec = request.session['ADMIN_SES']
       try:
              dbe = mysql.connect(host="127.0.0.1", port=3306,
                                  user="root", password='', db="songvideo")
              cmd = dbe.cursor()
              q="select * from subcategory"
              cmd.execute(q)
              srows=cmd.fetchall()
              dbe.close()
              return render(request, "showsubcategory.html",{'srows':srows})
       except Exception as e:
              print(e)
              return render(request, "showsubcategory.html",{'srows':[]})
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