from django.shortcuts import render
from .forms import FormContatti
from django.http import HttpResponse



# Create your views here.


# def viewContatti(request):
#     formContatti = FormContatti()
#     context = {"form":formContatti}
#     return render(request,"contatti.html", context)

def viewContatti(request):
    if request.method == "POST":
        formContatti = FormContatti(request.POST)
        if formContatti.is_valid():
            new_message = formContatti.save()
            return HttpResponse(f"""
            <div class="modal" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p>Grazie per averci contattato!</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

            """)
    else:
        formContatti = FormContatti()
    context = {"form":formContatti}
    return render(request,"contatti.html", context)
