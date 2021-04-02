from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Listing
# Create your views here.


def index(request):
    # list_date order and is_published has to be checked
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)  # 3 per page
    page = request.GET.get('page')  # page is url parameter
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # pk = primary key
    # get_object_or_404 : if there is passed listing id it will shows otherwise, it will display 404 error.
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
