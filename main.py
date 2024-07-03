from frictionless import formats, describe, Package, Schema
from pathlib import Path
from sqlalchemy import MetaData
from models import engine
import os

control = formats.SqlControl()
path = 'sqlite:///database.db'
metadata = MetaData()
metadata.reflect(engine)
table_names = list(metadata.tables.keys())
table_names.reverse()
# import ipdb; ipdb.set_trace(context=10)

dataset_path = Path(__file__).parent / 'dataset'
datapackage_yaml = dataset_path / 'datapackage.yaml'
package = Package(datapackage_yaml)

import ipdb; ipdb.set_trace(context=10)

for name in table_names:
    schema_path = dataset_path / 'schemas' / f'{name}.yaml'
    schema_yaml = Schema(schema_path)
    control = formats.SqlControl(table=name, basepath='data')
    schema = describe(path=path, name =name, control=control, type="resource")
    for field in schema.field_names:
        schema.get_field(field)
    package.add_resource(schema)
    print(schema.to_yaml())

package.to_er_diagram(path='erd.dot')
os.system("dot -Tpng erd.dot > package_erd.png")
