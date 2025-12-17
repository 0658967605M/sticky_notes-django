from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.all().order_by("-created_at")
    return render(request, "sticky_notes_app/home.html", {"notes": notes})


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NoteForm()
    return render(request, "sticky_notes_app/note_form.html", {"form": form})


def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NoteForm(instance=note)
    return render(request, "sticky_notes_app/note_form.html", {"form": form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("home")
    return render(
        request,
        "sticky_notes_app/note_confirm_delete.html",
        {"note": note},
    )
