"""musicvid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import category
from . import subcategory
from . import songs
from . import Admin
from . import user
from . import userlogin
urlpatterns = [

    path('admin/', admin.site.urls),
    path('categoryinterface/', category.ActionCategoryInterface),
    path('categorysubmit', category.ActionSubmitCategory),
    path('categorydisplayall',category.ActionDisplayAll),
    path('categorydisplaybyid/',category.ActionDisplayByid),
    path('showcategory/',category.ActionShowCategory),
    path('showsongs/',category.ActionShowSongs),
    path('showallsongs/',songs.ActionShowAllSongs),
    path('categoryeditdeletesubmit', category.ActionCategoryEditDeleteSubmit),
    path('editcategorypicture', category.ActionEditCategoryPicture),
    path('subcategoryinterface/', subcategory.ActionSubCategoryInterface),
    path('subcategorysubmit', subcategory.ActionSubmitSubCategory),
    path('subcategorydisplayall',subcategory.ActionSubCategoryDisplayAll),
    path('subcategorydisplaybyid/', subcategory.ActionSubCategoryDisplayByid),
    path('showsubcategory/', category.ActionShowSubCategory),
    path('showallsubcategory/', subcategory.ActionShowSubCategory),
    path('showsongs/', subcategory.ActionShowSongs),
    path('subcategoryeditdeletesubmit', subcategory.ActionSubCategoryEditDeleteSubmit),
    path('editsubcategorypicture', subcategory.ActionEditSubCategoryPicture),
    path('songsinterface/',songs.ActionSongsInterface),
    path('songssubmit', songs.ActionSubmitSongs),
    path('songsdisplayall',songs.ActionSongsDisplayAll),
    path('songsdisplaybyid/', songs.ActionSongsDisplayByid),
    path('songseditdeletesubmit', songs.ActionSongsEditDeleteSubmit),
    path('editsongspicture', songs.ActionEditSongsPicture),
    path('admininterface/', Admin.ActionAdminLogin),
    path('checkadminlogin', Admin.ActionCheckLogin),
    path('categorydisplayalljson/',category.ActionDisplayJson),
    path('displaysubcategoryjson/',songs.ActionDisplaySubCategoryJson),
    path('mainpage/',user.ActionMainInterface),
    path('categorypage/', user.ActionCategoryPage),
    path('playlistpage/', user.ActionPlaylistPage),
    path('artistpage/', user.ActionArtistPage),
    path('subcategorypage/', user.ActionSubCategoryPage),
    path('searchsongpage/',user.ActionSearchSongPage),
    path('searchsongjson/', user.ActionSearchSongJson),
    path('playsong/', user.ActionPlaySong),
    path('logout/', Admin.ActionLogout),
    path('contact/',user.ActionContact),
    path('blog/',user.Actionblog),
    path('submitmessage',user.ActionContactmessage),
    path('messagedisplayall',category.Actionmessagedisplay),
    path('createacc',userlogin.ActionUserCREATEACC),
    path('acccreate',userlogin.ActionInsertacc),
    path('login', userlogin.ActionUSERLogin),
    path('userlogin',userlogin.ActionUserlogin),
    path('usermainpage/',userlogin.ActionUserMainInterface),
    path('userlogout/', userlogin.ActionLogoutUser),
    path('usercategorypage/', userlogin.ActionUserCategoryPage),
    path('userplaylistpage/', userlogin.ActionUserPlaylistPage),
    path('userartistpage/', user.ActionArtistPage),
    path('usersubcategorypage/', userlogin.ActionUserSubCategoryPage),
    path('usersearchsongpage/', userlogin.ActionUserSearchSongPage),
    path('usersearchsongjson/', userlogin.ActionUserSearchSongJson),
    path('userplaysong/',userlogin.ActionUserPlaySong),
    path('usercontact/', userlogin.ActionUserContact),
    path('usersubmitmessage', userlogin.ActionUserContactmessage),
    path('userblog/', userlogin.ActionUserblog),
    path('userhomepage/', userlogin.ActionUserMainInterface),


]
urlpatterns+=staticfiles_urlpatterns()
