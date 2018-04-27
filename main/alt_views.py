def case_lookup(request):
  if request.method == 'POST':
    url = reverse('case-details', kwargs={'case_id': request.POST['case-id']})
    return redirect(url)
  else:
    return render(request, 'case_lookup.html')

@login_required
def case_details(request, case_id=None):
  '''
    Removed from main app because it's not clear whether a Client would need to login
    to see Case details. They probably know what's going on through their correspondence
    with their Attorney.
  '''
  if request.method == 'GET':
    c = Case.objects.get(case_id=case_id)
    return render(
      request,
      'case.html',
      {
        'opened_on': c.opened_on,
        'attorney': c.attorney.name,
        'case_id': c.case_id,
        'is_open': c.is_open,
        'closed_on': c.closed_on
      }
    )
  else:
    url = reverse('case-lookup')
    return redirect(url)