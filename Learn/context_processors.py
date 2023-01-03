
def cev_pros(request):

    isins=request.user.groups.filter(name='Instructor').exists()
    return {"isins":isins}