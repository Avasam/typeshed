from _typeshed import Incomplete
from typing import NamedTuple

from ..util import memoized_property
from . import elements

RESERVED_WORDS: Incomplete
LEGAL_CHARACTERS: Incomplete
LEGAL_CHARACTERS_PLUS_SPACE: Incomplete
ILLEGAL_INITIAL_CHARACTERS: Incomplete
FK_ON_DELETE: Incomplete
FK_ON_UPDATE: Incomplete
FK_INITIALLY: Incomplete
BIND_PARAMS: Incomplete
BIND_PARAMS_ESC: Incomplete
BIND_TEMPLATES: Incomplete
OPERATORS: Incomplete
FUNCTIONS: Incomplete
EXTRACT_MAP: Incomplete
COMPOUND_KEYWORDS: Incomplete
RM_RENDERED_NAME: int
RM_NAME: int
RM_OBJECTS: int
RM_TYPE: int

class ExpandedState(NamedTuple):
    statement: Incomplete
    additional_parameters: Incomplete
    processors: Incomplete
    positiontup: Incomplete
    parameter_expansion: Incomplete

NO_LINTING: Incomplete
COLLECT_CARTESIAN_PRODUCTS: Incomplete
WARN_LINTING: Incomplete
FROM_LINTING: Incomplete

class FromLinter:
    def lint(self, start: Incomplete | None = ...): ...
    def warn(self) -> None: ...

class Compiled:
    schema_translate_map: Incomplete
    execution_options: Incomplete
    compile_state: Incomplete
    cache_key: Incomplete
    dialect: Incomplete
    preparer: Incomplete
    statement: Incomplete
    can_execute: Incomplete
    string: Incomplete
    def __init__(
        self,
        dialect,
        statement,
        schema_translate_map: Incomplete | None = ...,
        render_schema_translate: bool = ...,
        compile_kwargs=...,
    ) -> None: ...
    def visit_unsupported_compilation(self, element, err) -> None: ...
    @property
    def sql_compiler(self) -> None: ...
    def process(self, obj, **kwargs): ...
    def construct_params(
        self, params: Incomplete | None = ..., extracted_parameters: Incomplete | None = ..., escape_names: bool = ...
    ) -> None: ...
    @property
    def params(self): ...

class TypeCompiler:
    ensure_kwarg: str
    dialect: Incomplete
    def __init__(self, dialect) -> None: ...
    def process(self, type_, **kw): ...
    def visit_unsupported_compilation(self, element, err, **kw) -> None: ...

class _CompileLabel(elements.ColumnElement):
    __visit_name__: str
    element: Incomplete
    name: Incomplete
    def __init__(self, col, name, alt_names=...) -> None: ...
    @property
    def proxy_set(self): ...
    @property
    def type(self): ...
    def self_group(self, **kw): ...

class SQLCompiler(Compiled):
    extract_map: Incomplete
    compound_keywords: Incomplete
    isdelete: bool
    isinsert: bool
    isupdate: bool
    isplaintext: bool
    returning: Incomplete
    returning_precedes_values: bool
    render_table_with_column_in_update_from: bool
    ansi_bind_rules: bool
    insert_single_values_expr: Incomplete
    literal_execute_params: Incomplete
    post_compile_params: Incomplete
    escaped_bind_names: Incomplete
    has_out_parameters: bool
    insert_prefetch: Incomplete
    update_prefetch: Incomplete
    postfetch_lastrowid: bool
    positiontup: Incomplete
    inline: bool
    column_keys: Incomplete
    cache_key: Incomplete
    for_executemany: Incomplete
    linting: Incomplete
    binds: Incomplete
    bind_names: Incomplete
    stack: Incomplete
    positional: Incomplete
    bindtemplate: Incomplete
    ctes: Incomplete
    label_length: Incomplete
    anon_map: Incomplete
    truncated_names: Incomplete
    def __init__(
        self,
        dialect,
        statement,
        cache_key: Incomplete | None = ...,
        column_keys: Incomplete | None = ...,
        for_executemany: bool = ...,
        linting=...,
        **kwargs,
    ) -> None: ...
    @property
    def current_executable(self): ...
    @property
    def prefetch(self): ...
    def is_subquery(self): ...
    @property
    def sql_compiler(self): ...
    def construct_params(self, params: Incomplete | None = ..., _group_number: Incomplete | None = ..., _check: bool = ..., extracted_parameters: Incomplete | None = ..., escape_names: bool = ...): ...  # type: ignore[override]
    @property
    def params(self): ...
    def default_from(self): ...
    def visit_grouping(self, grouping, asfrom: bool = ..., **kwargs): ...
    def visit_select_statement_grouping(self, grouping, **kwargs): ...
    def visit_label_reference(self, element, within_columns_clause: bool = ..., **kwargs): ...
    def visit_textual_label_reference(self, element, within_columns_clause: bool = ..., **kwargs): ...
    def visit_label(
        self,
        label,
        add_to_result_map: Incomplete | None = ...,
        within_label_clause: bool = ...,
        within_columns_clause: bool = ...,
        render_label_as_label: Incomplete | None = ...,
        result_map_targets=...,
        **kw,
    ): ...
    def visit_lambda_element(self, element, **kw): ...
    def visit_column(
        self, column, add_to_result_map: Incomplete | None = ..., include_table: bool = ..., result_map_targets=..., **kwargs
    ): ...
    def visit_collation(self, element, **kw): ...
    def visit_fromclause(self, fromclause, **kwargs): ...
    def visit_index(self, index, **kwargs): ...
    def visit_typeclause(self, typeclause, **kw): ...
    def post_process_text(self, text): ...
    def escape_literal_column(self, text): ...
    def visit_textclause(self, textclause, add_to_result_map: Incomplete | None = ..., **kw): ...
    def visit_textual_select(self, taf, compound_index: Incomplete | None = ..., asfrom: bool = ..., **kw): ...
    def visit_null(self, expr, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def visit_tuple(self, clauselist, **kw): ...
    def visit_clauselist(self, clauselist, **kw): ...
    def visit_case(self, clause, **kwargs): ...
    def visit_type_coerce(self, type_coerce, **kw): ...
    def visit_cast(self, cast, **kwargs): ...
    def visit_over(self, over, **kwargs): ...
    def visit_withingroup(self, withingroup, **kwargs): ...
    def visit_funcfilter(self, funcfilter, **kwargs): ...
    def visit_extract(self, extract, **kwargs): ...
    def visit_scalar_function_column(self, element, **kw): ...
    def visit_function(self, func, add_to_result_map: Incomplete | None = ..., **kwargs): ...
    def visit_next_value_func(self, next_value, **kw): ...
    def visit_sequence(self, sequence, **kw) -> None: ...
    def function_argspec(self, func, **kwargs): ...
    compile_state: Incomplete
    def visit_compound_select(self, cs, asfrom: bool = ..., compound_index: Incomplete | None = ..., **kwargs): ...
    def visit_unary(self, unary, add_to_result_map: Incomplete | None = ..., result_map_targets=..., **kw): ...
    def visit_is_true_unary_operator(self, element, operator, **kw): ...
    def visit_is_false_unary_operator(self, element, operator, **kw): ...
    def visit_not_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_in_op_binary(self, binary, operator, **kw): ...
    def visit_empty_set_op_expr(self, type_, expand_op): ...
    def visit_empty_set_expr(self, element_types) -> None: ...
    def visit_binary(
        self,
        binary,
        override_operator: Incomplete | None = ...,
        eager_grouping: bool = ...,
        from_linter: Incomplete | None = ...,
        lateral_from_linter: Incomplete | None = ...,
        **kw,
    ): ...
    def visit_function_as_comparison_op_binary(self, element, operator, **kw): ...
    def visit_mod_binary(self, binary, operator, **kw): ...
    def visit_custom_op_binary(self, element, operator, **kw): ...
    def visit_custom_op_unary_operator(self, element, operator, **kw): ...
    def visit_custom_op_unary_modifier(self, element, operator, **kw): ...
    def visit_contains_op_binary(self, binary, operator, **kw): ...
    def visit_not_contains_op_binary(self, binary, operator, **kw): ...
    def visit_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_endswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_endswith_op_binary(self, binary, operator, **kw): ...
    def visit_like_op_binary(self, binary, operator, **kw): ...
    def visit_not_like_op_binary(self, binary, operator, **kw): ...
    def visit_ilike_op_binary(self, binary, operator, **kw): ...
    def visit_not_ilike_op_binary(self, binary, operator, **kw): ...
    def visit_between_op_binary(self, binary, operator, **kw): ...
    def visit_not_between_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw) -> None: ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw) -> None: ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw) -> None: ...
    def visit_bindparam(
        self,
        bindparam,
        within_columns_clause: bool = ...,
        literal_binds: bool = ...,
        skip_bind_expression: bool = ...,
        literal_execute: bool = ...,
        render_postcompile: bool = ...,
        **kwargs,
    ): ...
    def render_literal_bindparam(
        self, bindparam, render_literal_value=..., bind_expression_template: Incomplete | None = ..., **kw
    ): ...
    def render_literal_value(self, value, type_): ...
    def bindparam_string(
        self,
        name,
        positional_names: Incomplete | None = ...,
        post_compile: bool = ...,
        expanding: bool = ...,
        escaped_from: Incomplete | None = ...,
        **kw,
    ): ...
    execution_options: Incomplete
    ctes_recursive: bool
    def visit_cte(
        self,
        cte,
        asfrom: bool = ...,
        ashint: bool = ...,
        fromhints: Incomplete | None = ...,
        visiting_cte: Incomplete | None = ...,
        from_linter: Incomplete | None = ...,
        **kwargs,
    ): ...
    def visit_table_valued_alias(self, element, **kw): ...
    def visit_table_valued_column(self, element, **kw): ...
    def visit_alias(
        self,
        alias,
        asfrom: bool = ...,
        ashint: bool = ...,
        iscrud: bool = ...,
        fromhints: Incomplete | None = ...,
        subquery: bool = ...,
        lateral: bool = ...,
        enclosing_alias: Incomplete | None = ...,
        from_linter: Incomplete | None = ...,
        **kwargs,
    ): ...
    def visit_subquery(self, subquery, **kw): ...
    def visit_lateral(self, lateral_, **kw): ...
    def visit_tablesample(self, tablesample, asfrom: bool = ..., **kw): ...
    def visit_values(self, element, asfrom: bool = ..., from_linter: Incomplete | None = ..., **kw): ...
    def get_render_as_alias_suffix(self, alias_name_text): ...
    def format_from_hint_text(self, sqltext, table, hint, iscrud): ...
    def get_select_hint_text(self, byfroms) -> None: ...
    def get_from_hint_text(self, table, text) -> None: ...
    def get_crud_hint_text(self, table, text) -> None: ...
    def get_statement_hint_text(self, hint_texts): ...
    translate_select_structure: Incomplete
    def visit_select(
        self,
        select_stmt,
        asfrom: bool = ...,
        insert_into: bool = ...,
        fromhints: Incomplete | None = ...,
        compound_index: Incomplete | None = ...,
        select_wraps_for: Incomplete | None = ...,
        lateral: bool = ...,
        from_linter: Incomplete | None = ...,
        **kwargs,
    ): ...
    def get_cte_preamble(self, recursive): ...
    def get_select_precolumns(self, select, **kw): ...
    def group_by_clause(self, select, **kw): ...
    def order_by_clause(self, select, **kw): ...
    def for_update_clause(self, select, **kw): ...
    def returning_clause(self, stmt, returning_cols) -> None: ...
    def limit_clause(self, select, **kw): ...
    def fetch_clause(self, select, **kw): ...
    def visit_table(
        self,
        table,
        asfrom: bool = ...,
        iscrud: bool = ...,
        ashint: bool = ...,
        fromhints: Incomplete | None = ...,
        use_schema: bool = ...,
        from_linter: Incomplete | None = ...,
        **kwargs,
    ): ...
    def visit_join(self, join, asfrom: bool = ..., from_linter: Incomplete | None = ..., **kwargs): ...
    def visit_insert(self, insert_stmt, **kw): ...
    def update_limit_clause(self, update_stmt) -> None: ...
    def update_tables_clause(self, update_stmt, from_table, extra_froms, **kw): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> None: ...
    def visit_update(self, update_stmt, **kw): ...
    def delete_extra_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> None: ...
    def delete_table_clause(self, delete_stmt, from_table, extra_froms): ...
    def visit_delete(self, delete_stmt, **kw): ...
    def visit_savepoint(self, savepoint_stmt): ...
    def visit_rollback_to_savepoint(self, savepoint_stmt): ...
    def visit_release_savepoint(self, savepoint_stmt): ...

class StrSQLCompiler(SQLCompiler):
    def visit_unsupported_compilation(self, element, err, **kw): ...
    def visit_getitem_binary(self, binary, operator, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_sequence(self, seq, **kw): ...
    def returning_clause(self, stmt, returning_cols): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...
    def delete_extra_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...
    def visit_empty_set_expr(self, type_): ...
    def get_from_hint_text(self, table, text): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw): ...

class DDLCompiler(Compiled):
    @memoized_property
    def sql_compiler(self): ...
    @memoized_property
    def type_compiler(self): ...
    def construct_params(
        self, params: Incomplete | None = ..., extracted_parameters: Incomplete | None = ..., escape_names: bool = ...
    ) -> None: ...
    def visit_ddl(self, ddl, **kwargs): ...
    def visit_create_schema(self, create, **kw): ...
    def visit_drop_schema(self, drop, **kw): ...
    def visit_create_table(self, create, **kw): ...
    def visit_create_column(self, create, first_pk: bool = ..., **kw): ...
    def create_table_constraints(self, table, _include_foreign_key_constraints: Incomplete | None = ..., **kw): ...
    def visit_drop_table(self, drop, **kw): ...
    def visit_drop_view(self, drop, **kw): ...
    def visit_create_index(self, create, include_schema: bool = ..., include_table_schema: bool = ..., **kw): ...
    def visit_drop_index(self, drop, **kw): ...
    def visit_add_constraint(self, create, **kw): ...
    def visit_set_table_comment(self, create, **kw): ...
    def visit_drop_table_comment(self, drop, **kw): ...
    def visit_set_column_comment(self, create, **kw): ...
    def visit_drop_column_comment(self, drop, **kw): ...
    def get_identity_options(self, identity_options): ...
    def visit_create_sequence(self, create, prefix: Incomplete | None = ..., **kw): ...
    def visit_drop_sequence(self, drop, **kw): ...
    def visit_drop_constraint(self, drop, **kw): ...
    def get_column_specification(self, column, **kwargs): ...
    def create_table_suffix(self, table): ...
    def post_create_table(self, table): ...
    def get_column_default_string(self, column): ...
    def visit_table_or_column_check_constraint(self, constraint, **kw): ...
    def visit_check_constraint(self, constraint, **kw): ...
    def visit_column_check_constraint(self, constraint, **kw): ...
    def visit_primary_key_constraint(self, constraint, **kw): ...
    def visit_foreign_key_constraint(self, constraint, **kw): ...
    def define_constraint_remote_table(self, constraint, table, preparer): ...
    def visit_unique_constraint(self, constraint, **kw): ...
    def define_constraint_cascades(self, constraint): ...
    def define_constraint_deferrability(self, constraint): ...
    def define_constraint_match(self, constraint): ...
    def visit_computed_column(self, generated, **kw): ...
    def visit_identity_column(self, identity, **kw): ...

class GenericTypeCompiler(TypeCompiler):
    def visit_FLOAT(self, type_, **kw): ...
    def visit_REAL(self, type_, **kw): ...
    def visit_NUMERIC(self, type_, **kw): ...
    def visit_DECIMAL(self, type_, **kw): ...
    def visit_INTEGER(self, type_, **kw): ...
    def visit_SMALLINT(self, type_, **kw): ...
    def visit_BIGINT(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_DATETIME(self, type_, **kw): ...
    def visit_DATE(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_CLOB(self, type_, **kw): ...
    def visit_NCLOB(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_NCHAR(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_NVARCHAR(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_BLOB(self, type_, **kw): ...
    def visit_BINARY(self, type_, **kw): ...
    def visit_VARBINARY(self, type_, **kw): ...
    def visit_BOOLEAN(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_boolean(self, type_, **kw): ...
    def visit_time(self, type_, **kw): ...
    def visit_datetime(self, type_, **kw): ...
    def visit_date(self, type_, **kw): ...
    def visit_big_integer(self, type_, **kw): ...
    def visit_small_integer(self, type_, **kw): ...
    def visit_integer(self, type_, **kw): ...
    def visit_real(self, type_, **kw): ...
    def visit_float(self, type_, **kw): ...
    def visit_numeric(self, type_, **kw): ...
    def visit_string(self, type_, **kw): ...
    def visit_unicode(self, type_, **kw): ...
    def visit_text(self, type_, **kw): ...
    def visit_unicode_text(self, type_, **kw): ...
    def visit_enum(self, type_, **kw): ...
    def visit_null(self, type_, **kw) -> None: ...
    def visit_type_decorator(self, type_, **kw): ...
    def visit_user_defined(self, type_, **kw): ...

class StrSQLTypeCompiler(GenericTypeCompiler):
    def process(self, type_, **kw): ...
    def __getattr__(self, key: str): ...
    def visit_null(self, type_, **kw): ...
    def visit_user_defined(self, type_, **kw): ...

class IdentifierPreparer:
    reserved_words: Incomplete
    legal_characters: Incomplete
    illegal_initial_characters: Incomplete
    schema_for_object: Incomplete
    dialect: Incomplete
    initial_quote: Incomplete
    final_quote: Incomplete
    escape_quote: Incomplete
    escape_to_quote: Incomplete
    omit_schema: Incomplete
    quote_case_sensitive_collations: Incomplete
    def __init__(
        self,
        dialect,
        initial_quote: str = ...,
        final_quote: Incomplete | None = ...,
        escape_quote: str = ...,
        quote_case_sensitive_collations: bool = ...,
        omit_schema: bool = ...,
    ) -> None: ...
    def validate_sql_phrase(self, element, reg): ...
    def quote_identifier(self, value): ...
    def quote_schema(self, schema, force: Incomplete | None = ...): ...
    def quote(self, ident, force: Incomplete | None = ...): ...
    def format_collation(self, collation_name): ...
    def format_sequence(self, sequence, use_schema: bool = ...): ...
    def format_label(self, label, name: Incomplete | None = ...): ...
    def format_alias(self, alias, name: Incomplete | None = ...): ...
    def format_savepoint(self, savepoint, name: Incomplete | None = ...): ...
    def format_constraint(self, constraint, _alembic_quote: bool = ...): ...
    def truncate_and_render_index_name(self, name, _alembic_quote: bool = ...): ...
    def truncate_and_render_constraint_name(self, name, _alembic_quote: bool = ...): ...
    def format_index(self, index): ...
    def format_table(self, table, use_schema: bool = ..., name: Incomplete | None = ...): ...
    def format_schema(self, name): ...
    def format_label_name(self, name, anon_map: Incomplete | None = ...): ...
    def format_column(
        self,
        column,
        use_table: bool = ...,
        name: Incomplete | None = ...,
        table_name: Incomplete | None = ...,
        use_schema: bool = ...,
        anon_map: Incomplete | None = ...,
    ): ...
    def format_table_seq(self, table, use_schema: bool = ...): ...
    def unformat_identifiers(self, identifiers): ...
