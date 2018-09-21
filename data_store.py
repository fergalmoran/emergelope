# Imports the Google Cloud client library
from google.cloud import datastore


def save_number(key, number):
    # Instantiates a client
    client = datastore.Client()

    kind = 'Number'
    name = key
    task_key = client.key(kind, name)

    task = datastore.Entity(key=task_key)
    task['number'] = number

    client.put(task)

    print('Saved {}: {}'.format(task.key.name, task['number']))


def list_numbers():
    client = datastore.Client()
    query = client.query(kind='Number')

    return list(query.fetch())


if __name__ == '__main__':
    print(list_numbers())
