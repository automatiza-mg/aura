from frictionless import formats, describe, Package
from sqlalchemy import MetaData
from models import engine
import os

control = formats.SqlControl()
path = 'sqlite:///database.db'
metadata = MetaData()
metadata.reflect(engine)
table_names = list(metadata.tables.keys())
table_names.reverse()
package = Package(name='teste')

for name in table_names:
    control = formats.SqlControl(table=name, basepath='data')
    schema = describe(path=path, name =name, control=control, type="resource")
    package.add_resource(schema)
    print(schema.to_yaml())

package.to_er_diagram(path='erd.dot')
os.system("dot -Tpng erd.dot > package_erd.png")
