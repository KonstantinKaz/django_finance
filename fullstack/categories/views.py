from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *

def category_list(request):
    expense_categories = ExpenseCategory.objects.all()
    income_categories = IncomeCategory.objects.all()
    return render(request, 'categories/category_list.html', {'expense_categories': expense_categories, 'income_categories': income_categories})


def expense_category_create(request):
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ExpenseCategoryForm()
    return render(request, 'categories/expense_category_create.html', {'form': form})


def expense_category_update(request, category_id):
    category = get_object_or_404(ExpenseCategory, category_id=category_id)
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ExpenseCategoryForm(instance=category)
    return render(request, 'categories/expense_category_update.html', {'form': form, 'category': category})


def expense_category_delete(request, category_id):
    category = get_object_or_404(ExpenseCategory, category_id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/expense_category_delete.html', {'category': category})


def income_category_create(request):
    if request.method == 'POST':
        form = IncomeCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = IncomeCategoryForm()
    return render(request, 'categories/income_category_create.html', {'form': form})


def income_category_update(request, category_id):
    category = get_object_or_404(IncomeCategory, category_id=category_id)
    if request.method == 'POST':
        form = IncomeCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = IncomeCategoryForm(instance=category)
    return render(request, 'categories/income_category_update.html', {'form': form, 'category': category})


def income_category_delete(request, category_id):
    category = get_object_or_404(IncomeCategory, category_id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/income_category_delete.html', {'category': category})
