from django.shortcuts import render


def aboutus(request):
    return render(
        request,
        "aboutus/",
    )


def faq(request):
    return render(
        request,
        "aboutus/faq.html/",
    )
