# coding=utf-8
"""empty message

Revision ID: 389881771619
Revises: None
Create Date: 2015-06-19 23:26:04.865597

"""

# revision identifiers, used by Alembic.
revision = '389881771619'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    enum_values_table = op.create_table('enum_values',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('code', sa.String(length=16), nullable=True),
    sa.Column('display', sa.String(length=16), nullable=False),
    sa.ForeignKeyConstraint(['type_id'], ['enum_values.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    )
    from sqlalchemy.sql import text
    op.bulk_insert(enum_values_table, [
        {'id':1, 'type_id':None, 'code':'BASIC_ENUM_TYPES', 'display':u'基本枚举类型'},
        {'id':2, 'type_id':1, 'code':'EXP_STATUS', 'display':u'支出状态'},
        {'id':3, 'type_id':1, 'code':'EXP_TYPE', 'display':u'支出类型'},
        {'id':4, 'type_id':1, 'code':'INCOMING_STATUS', 'display':u'收入状态'},
        {'id':5, 'type_id':1, 'code':'INCOMING_TYPE', 'display':u'收入类型'},
    ], multiinsert=False)
    op.get_bind().execute(text("ALTER SEQUENCE enum_values_id_seq RESTART WITH 6;"))
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=8), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['product_category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sales_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logistic_amount', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=True),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=8), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('qq', sa.String(length=16), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('contact', sa.String(length=16), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('website', sa.String(length=64), nullable=True),
    sa.Column('whole_sale_req', sa.String(length=32), nullable=True),
    sa.Column('can_mixed_whole_sale', sa.Boolean(), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('name')
    )
    op.create_table('incoming',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False),
    sa.Column('cate', sa.DateTime(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('sales_order_id', sa.Integer(), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['enum_values.id'], ),
    sa.ForeignKeyConstraint(['sales_order_id'], ['sales_order.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['enum_values.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_method',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_name', sa.String(length=8), nullable=False),
    sa.Column('account_number', sa.String(length=32), nullable=False),
    sa.Column('bank_name', sa.String(length=16), nullable=False),
    sa.Column('bank_branch', sa.String(length=32), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=8), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('deliver_day', sa.Integer(), nullable=True),
    sa.Column('lead_day', sa.Integer(), nullable=True),
    sa.Column('distinguishing_feature', sa.Text(), nullable=True),
    sa.Column('spec_link', sa.String(length=64), nullable=True),
    sa.Column('purchase_price', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=True),
    sa.Column('retail_price', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['product_category.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('name')
    )
    op.create_table('purchase_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logistic_amount', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=True),
    sa.Column('other_amount', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=True),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expense',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('amount', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False),
    sa.Column('has_invoice', sa.Boolean(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('purchase_order_id', sa.Integer(), nullable=True),
    sa.Column('sales_order_id', sa.Integer(), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['enum_values.id'], ),
    sa.ForeignKeyConstraint(['purchase_order_id'], ['purchase_order.id'], ),
    sa.ForeignKeyConstraint(['sales_order_id'], ['sales_order.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['enum_values.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase_order_line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False),
    sa.Column('quantity', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False),
    sa.Column('purchase_order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['purchase_order_id'], ['purchase_order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sales_order_line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False),
    sa.Column('quantity', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False),
    sa.Column('original_amount', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=True),
    sa.Column('adjust_amount', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=True),
    sa.Column('actual_amount', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=True),
    sa.Column('sales_order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['sales_order_id'], ['sales_order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales_order_line')
    op.drop_table('purchase_order_line')
    op.drop_table('expense')
    op.drop_table('purchase_order')
    op.drop_table('product')
    op.drop_table('payment_method')
    op.drop_table('incoming')
    op.drop_table('supplier')
    op.drop_table('sales_order')
    op.drop_table('product_category')
    op.drop_table('enum_values')
    ### end Alembic commands ###
