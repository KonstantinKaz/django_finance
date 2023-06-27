from django.shortcuts import render, get_object_or_404, redirect
from .models import Goal
from .forms import GoalForm
from balance.models import Balance
from django.shortcuts import redirect

def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    context = {'goals': goals}
    return render(request, 'goals/goal_list.html', context)


def calculate_remaining_amount(goal):
    balance = Balance.objects.get(user=goal.user)
    remaining_amount = goal.amount - balance.total_balance
    return remaining_amount

def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goal_list')
    else:
        form = GoalForm()

    context = {'form': form}
    return render(request, 'goals/goal_form.html', context)


def goal_update(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    else:
        form = GoalForm(instance=goal)
    context = {'form': form}
    return render(request, 'goals/goal_form.html', context)

def goal_delete(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    goal.delete()
    return redirect('goal_list')


