from flask import render_template
from app import application
from app.utils.i18n import I18n

i18n = I18n('translate')


@application.route('/', methods=['GET'])
def root_index():
    i18n.set_locale('jp')
    return render_template('root/index.html', i18n=i18n)
