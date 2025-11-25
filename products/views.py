from django.shortcuts import render

# Vista de productos
def product_list(request):
    """
    Vista que muestra el listado de todos los productos disponibles
    """
    products = [
        {
            'id': 1,
            'name': 'Laptop HP',
            'price': 15000,
            'description': 'Laptop HP con procesador Intel Core i5',
            'image': 'https://imgs.search.brave.com/BAoXKKf__WUMMKUfQTRFhoNqrWE7ZYeQUvLkAK-bQFs/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWpv/cmxhcHRvcC5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMTgv/MDQvU2Ftc3VuZy1D/aHJvbWVib29rLTMt/TWVqb3Jlcy1sYXB0/b3BzLXBvci1tZW5v/cy1kZS0yMDAtZG9s/YXJlcy5qcGc'
        },
        {
            'id': 2,
            'name': 'Mouse Logitech',
            'price': 350,
            'description': 'Mouse inalámbrico Logitech',
            'image': 'https://imgs.search.brave.com/BAoXKKf__WUMMKUfQTRFhoNqrWE7ZYeQUvLkAK-bQFs/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWpv/cmxhcHRvcC5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMTgv/MDQvU2Ftc3VuZy1D/aHJvbWVib29rLTMt/TWVqb3Jlcy1sYXB0/b3BzLXBvci1tZW5v/cy1kZS0yMDAtZG9s/YXJlcy5qcGc'
        },
        {
            'id': 3,
            'name': 'Teclado Mecánico',
            'price': 1200,
            'description': 'Teclado mecánico RGB',
            'image': 'https://imgs.search.brave.com/BAoXKKf__WUMMKUfQTRFhoNqrWE7ZYeQUvLkAK-bQFs/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWpv/cmxhcHRvcC5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMTgv/MDQvU2Ftc3VuZy1D/aHJvbWVib29rLTMt/TWVqb3Jlcy1sYXB0/b3BzLXBvci1tZW5v/cy1kZS0yMDAtZG9s/YXJlcy5qcGc'
        },
    ]
    
    context = {
        'title': 'Productos - Django Store',
        'products': products,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, product_id):
    """
    Vista que muestra el detalle de un producto específico
    """
    # Datos del producto
    product = {
        'id': product_id,
        'name': 'Laptop HP',
        'price': 15000,
        'description': 'Laptop HP con procesador Intel Core i5, 8GB RAM, 256GB SSD',
        'image': 'https://imgs.search.brave.com/BAoXKKf__WUMMKUfQTRFhoNqrWE7ZYeQUvLkAK-bQFs/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWpv/cmxhcHRvcC5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMTgv/MDQvU2Ftc3VuZy1D/aHJvbWVib29rLTMt/TWVqb3Jlcy1sYXB0/b3BzLXBvci1tZW5v/cy1kZS0yMDAtZG9s/YXJlcy5qcGc',
        'stock': 10,
        'category': 'Electrónica'
    }
    
    context = {
        'title': f'{product["name"]} - Django Store',
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)