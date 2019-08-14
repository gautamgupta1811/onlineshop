def header():
    print(
        """
        <nav class="navbar navbar-expand-lg navbar-dark bg-danger">
  <a class="navbar-brand" href="index.py">Online Shop</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="index.py">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="products.py">All Products</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Product Category
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="catogery.py?q=mobile">Mobile</a>
          <a class="dropdown-item" href="catogery.py?q=laptop">Laptop</a>
          <a class="dropdown-item" href="catogery.py?q=book">Books</a>
          <a class="dropdown-item" href="catogery.py?q=headphone">Head Phones</a>
          <a class="dropdown-item" href="catogery.py?q=shoes">Shoes</a>
          <a class="dropdown-item" href="catogery.py?q=watch">Watch</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="cart.py" tabindex="-1" aria-disabled="true">My Cart</a>
      </li>
    </ul>
    <form action='search.py' class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" name='q' type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
""")

def footer():
    print("""
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
    </html>
    """)