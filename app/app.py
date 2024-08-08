from flask import Flask
import logging
import os


def create_app():

    app = Flask(__name__)
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="log.txt", level=logging.DEBUG)

    base_dir = os.path.abspath(os.path.dirname(__file__))
    cat_count_file = os.path.join(base_dir, 'cat_count.txt')

    global cat_count
    cat_count = 0

    with open(cat_count_file, 'r') as file:
        try:
            cat_count = int(file.read())
            logger.info('Reading cat_count.txt')
        except Exception as e:
            logger.error(e)
            logger.error('Error reading cat_count.txt! Reverting to 0...')

    @app.route('/get_cat_count')
    def get_cat_count():
        global cat_count

        with open(cat_count_file, 'r') as file:
            try:
                cat_count = int(file.read())
                logger.info('Reading cat_count.txt')
            except Exception as e:
                logger.error(e)
                logger.error('Error reading cat_count.txt! Reverting to 0...')

        logger.info('Cat count requested')
        return f'{cat_count}'

    @app.route('/increment_cat_count')
    def increment_cat_count():
        global cat_count
        cat_count += 1
        with open(cat_count_file, 'w') as fileA:
            fileA.write(str(cat_count))
            logger.info('Cat count incremented')

        return 'Cat count incremented'

    return app
    # if __name__ == '__main__':
    #     logger.info('API sever starting...')
    #     app.run()
