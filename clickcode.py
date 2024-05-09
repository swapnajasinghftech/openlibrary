import click
import requests

@click.command()
@click.argument('query')
def search_books(query):
    """Search books on Open Library."""
    url = f'http://openlibrary.org/search.json?q={query}'
    response = requests.get(url)
    data = response.json()

    if 'docs' in data:
        for book in data['docs']:
            click.echo(f"Title: {book.get('title', 'Unknown')}")
            click.echo(f"Author: {', '.join(book.get('author_name', ['Unknown']))}")
            click.echo()

if __name__ == '__main__':
    search_books()