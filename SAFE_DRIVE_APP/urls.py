
from django.contrib import admin
from django.urls import path

from SAFE_DRIVE_APP import views

urlpatterns = [
    path('home', views.home,name="home"),
    path('', views.first,name="first"),
    path('login', views.login,name="login"),
    path('logincode', views.logincode,name="logincode"),
    path('login_code', views.login_code,name="login_code"),

    path('editlocation/<int:id>',views.editlocation,name="editlocation"),
    path('editlocpost',views.editlocpost,name="editlocpost"),
    path('search_user',views.search_user,name="search_user"),
    path('search_ambulance',views.search_ambulance,name="search_ambulance"),
    path('dlt_poth/<int:id>',views.dlt_poth,name="dlt_poth"),




    path('addblind', views.addblind, name="addblind"),
    path('update_prof_ambulance', views.update_prof_ambulance, name="update_prof_ambulance"),
    # path('accident_notify', views.accident_notify, name="accident_notify"),
    path('add1',views.add1, name="add1"),
    path('addblindspot',views.addblindspot,name="addblindspot"),
    path('map',views.map,name="map"),
    path('map1',views.map1,name="map1"),
    path('addaccident',views.addaccident,name="addaccident"),

    # path('mapcode',views.mapcode,name="mapcode"),
    path('search_blind',views.search_blind,name="search_blind"),
    path('dltblind/<int:id>',views.dltblind,name="dltblind"),


    path('editblind/<int:id>',views.editblind,name="editblind"),
    path('editblindspot',views.editblindspot,name="editblindspot"),

    path('viewblind', views.viewblind, name="viewblind"),
    path('patholenottification', views.patholenottification, name="patholenottification"),
    path('pothole_noti_insertion', views.pothole_noti_insertion, name="pothole_noti_insertion"),
    path('update_prof', views.update_prof, name="update_prof"),
    path('view_profile', views.view_profile, name="view_profile"),
    path('view_profile_ambulance', views.view_profile_ambulance, name="view_profile_ambulance"),
    path('logoutcode', views.logoutcode, name="logoutcode"),
    path('delete_alert2', views.delete_alert2, name="delete_alert2"),
    path('view_myalert', views.view_myalert, name="view_myalert"),





    path('addlocation', views.addlocation, name="addlocation"),
    path('delete_alert', views.delete_alert, name="delete_alert"),

    path('view_potholealert',views. view_potholealert, name="view_potholealert"),

    path('addlocat',views.addlocat,name="addlocat"),
    path('addloc',views.addloc,name="addloc"),
    path('first',views.first,name="first"),
    path('search_loc',views.search_loc,name="search_loc"),
    path('dltloc/<int:id>',views.dltloc,name="dltloc"),
    path('calculate_age',views.calculate_age,name="calculate_age"),
    path('calculates_age',views.calculates_age,name="calculates_age"),
    path('search_acci',views.search_acci,name="search_acci"),

    path('viewlocation', views.viewlocation, name="viewlocation"),
    path('viewuser', views.viewuser, name="viewuser"),
    path('viewambulance', views.viewambulance, name="viewambulance"),
    path('verifyambulance', views.verifyambulance, name="verifyambulance"),
    path('viewaccident', views.viewaccident, name="viewaccident"),
    path('viewpothole', views.viewpothole, name="viewpothole"),
    path('viewfeed', views.viewfeed, name="viewfeed"),
    path('viewcomp', views.viewcomp, name="viewcomp"),
    path('sendreply/<int:id>', views.sendreply, name="sendreply"),
    path('adminhome', views.adminhome, name="adminhome"),
    path('admin_accept_ambulace/<id>', views.admin_accept_ambulace, name="admin_accept_ambulace"),
    path('reject_ambulance/<id>', views.reject_ambulance, name="reject_ambulance"),
    path('viewtraffic', views.viewtraffic, name="viewtraffic"),
    path('logout', views.logout, name="logout"),
    path('sendcomp', views.sendcomp, name="sendcomp"),
    path('searchpoth', views.searchpoth, name="searchpoth"),
    path('sendcompreply', views.sendcompreply, name="sendcompreply"),
    path('search_comp', views.search_comp, name="search_comp"),
    path('sview_location', views.sview_location, name="sview_location"),
    path('send_feed', views.send_feed, name="send_feed"),
    path('searchfeed', views.searchfeed, name="searchfeed"),
    path('view_alert', views.view_alert, name="view_alert"),
    path('update_status', views.update_status, name="update_status"),
    path('view_updated_accident', views.view_updated_accident, name="view_updated_accident"),



    path('registration', views.registration , name="registration"),
    path('registration2',views.registration2, name="registration2"),
    path('checkun',views.checkun, name="checkun"),
    path('updatelocation',views.updatelocation, name="updatelocation"),
    path('user_view_comp',views.user_view_comp, name="user_view_comp"),
    path('view_location',views.view_location, name="view_location"),




]
