"""Migración inicial

Revision ID: 4e7f5ea18f0b
Revises: 
Create Date: 2023-07-12 19:49:13.978100

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4e7f5ea18f0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nota',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=100), nullable=True),
    sa.Column('contenido', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('usuarios')
    op.drop_table('notas')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notas',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('titulo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('contenido', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('usuarios',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombreusuario', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('contraseña', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('correo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('idNotas', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['idNotas'], ['notas.id'], name='usuarios_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.drop_table('nota')
    # ### end Alembic commands ###
