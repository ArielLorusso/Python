
https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/
   
####      LIST OF Django.db  models.Model  FIELDS (methods)

```py       
AutoField	   # It is an IntegerField that automatically increments.
BigAutoField	# It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.
BigIntegerField#	It is a 64-bit integer, much like an IntegerField except that it is guaranteed to fit numbers from -9223372036854775808 to 9223372036854775807.
BinaryField	   # A field to store raw binary data. 
BooleanField	# A true/false field. 
The default    # form widget for this field is a CheckboxInput.
CharField	   # A field to store text-based values.
DateField   	# A date, represented in Python by a datetime.date instance
DateTimeField	# It is used for date and time, represented in Python by a datetime.datetime instance.
DecimalField	# It is a fixed-precision decimal number, represented in Python by a Decimal instance.
DurationField	# A field for storing periods of time.
EmailField	   # It is a CharField that checks that the value is a valid email address.
FileField	   # It is a file-upload field.
FloatField	   # It is a floating-point number represented in Python by a float instance.
ImageField	   # It inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
IntegerField	# It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.
GenericIPAddressField	# An IPv4 or IPv6 address, in string format (e.g. 192.0.2.30 or 2a02:42fe::4).
NullBooleanField	# Like a BooleanField, but allows NULL as one of the options.
PositiveIntegerField	# Like an IntegerField, but must be either positive or zero (0).
PositiveSmallIntegerField	# Like a PositiveIntegerField, but only allows values under a certain (database-dependent) point.
SlugField	# Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
SmallIntegerField	# It is like an IntegerField, but only allows values under a certain (database-dependent) point.
TextField	# A large text field. The default form widget for this field is a Textarea.
TimeField	# A time, represented in Python by a datetime.time instance.
URLField	   # A CharField for a URL, validated by URLValidator.
UUIDField	# A field for storing universally unique identifiers. Uses Python’s UUID class. When used on PostgreSQL, this stores in a uuid datatype, otherwise in a char(32).

#           RELATIONSHIP FIELDS :

ForeignKey	# A many-to-one relationship. Requires two positional arguments: 
# the class to which the model is related and the on_delete option.
ManyToManyField	# A many-to-many relationship. Requires a positional argument:
# the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships.
OneToOneField	# A one-to-one relationship. Conceptually, this is similar to a ForeignKey
# with unique=True, but the “reverse” side of the relation will directly return a single object.
```

####  django.db  models.Model     RELATIONSHIP Field Options	

```py                                                      FOREIGN KEY 
class ForeignKe :
ForeignKey(to, on_delete, **options)   # method ()
 # parameters :
ForeignKey.to_field
ForeignKey.on_delete
ForeignKey.swappable    True/False
ForeignKey.related_name
ForeignKey.db_constraint
ForeignKey.limit_choices_to
ForeignKey.related_query_name
class OneToOneField :
OneToOneField.parent_link
class ManyToManyField :
ManyToManyField(to, **options)
```

# Foreign class example

```py
class ArchiveModel(models.Model):
    # Define a ForeignKey field with swappable set to True
    some_foreign_key = models.ForeignKey(
        'OtherModel',
        on_delete=models.CASCADE,
        swappable=True,  # Set to True
    )
    # Other fields for your model
```

 https://devdocs.io/django~4.2/ref/models/fields#django.db.models.ForeignKey.swappable
 https://devdocs.io/django~4.2/ref/models/fields#django.db.models.ForeignKey

 
                                                    DONT CONFUSE   MODEL WITH FIELD
```py
class db_model__Field:
Field.many_to_many  # Boolean flag that is True if the field has a many-to-many relation; False otherwise. The only field included with Django where this is True is ManyToManyField.
Field.many_to_one # Boolean flag that is True if the field has a many-to-one relation, such as a ForeignKey; False otherwise.
Field.one_to_many # Boolean flag that is True if the field has a one-to-many relation, such as a GenericRelation or the reverse of a ForeignKey; False otherwise.
Field.one_to_one # Boolean flag that is True if the field has a one-to-one relation, such as a OneToOneField; False otherwise.
Field.related_model # Points to the model the field relates to. For example, Author in ForeignKey(Author, on_delete=models.CASCADE). The related_model for a GenericForeignKey is always None.
```


####  django.db  models.Model     Field Options	

https://www.geeksforgeeks.org/datefield-django-models/
https://devdocs.io/django~4.2/ref/models/fields#django.db.models.ForeignKey.on_delete
```py    FOREIGN KEY DELETION
CASCADE # Cascade deletes. Django emulates the behavior of the SQL constraint ON DELETE CASCADE  and also deletes the object containing the ForeignKey.  Model.delete() isn’t called on related models, but the pre_delete and post_delete signals are sent for all deleted objects.
PROTECT  # Prevent deletion of the referenced object by raising ProtectedError, a subclass of django.db.IntegrityError.
RESTRICT # Prevent deletion of the referenced object by raising RestrictedError (a subclass of django.db.IntegrityError). Unlike PROTECT, deletion of the referenced object is allowed if it also references a different object that is being deleted in the same operation, but via a CASCADE relationship.
SET_NULL # Set the ForeignKey null; this is only possible if null is True.
SET_DEFAULT #Set the ForeignKey to its default value; a default for the ForeignKey must be set.
SET() # Set the ForeignKey to the value passed to SET(), or if a callable is passed in, the result of calling it. In most cases, passing a callable will be necessary to avoid executing queries at the time your models.py is imported:
DO_NOTHING # Take no action. If your database backend enforces referential integrity, this will cause an IntegrityError unless you manually add an SQL ON DELETE constraint to the database field.
```

####  django.db  models.Model     Field Options	
```  py    
Null	      # If True, Django will store empty values as NULL in the database. Default is False.
Blank	      # If True, the field is allowed to be blank. Default is False.
db_column	# The name of the database column to use for this field. If this isn’t given, Django will use the field’s name. 
Default	   # The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object is created. 
help_text	# Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form. 
#primary_key	If True, this field is the primary key for the model.
editable	   # If False, the field will not be displayed in the admin or any other ModelForm. They are also skipped during model validation. Default is True. 
error_messages	# The error_messages argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override. 
help_text	# Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form. 
verbose_name# A human-readable name for the field. If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces. 
validators	# A list of validators to run for this field. See the validators documentation for more information. 
Unique	   # If True, this field must be unique throughout the table. 
```


https://devdocs.io/django~4.2-django-db-models/


db.models.Aggregate
db.models.Aggregate.allow_distinct
db.models.Aggregate.empty_result_set_value
db.models.Aggregate.function
db.models.Aggregate.template
db.models.Aggregate.window_compatible
db.models.as_sql()
db.models.as_vendorname()
db.models.AutoField
db.models.Avg
db.models.Avg.distinct
db.models.BaseConstraint
db.models.BaseConstraint.name
db.models.BaseConstraint.validate()
db.models.BaseConstraint.violation_error_message
db.models.BigAutoField
db.models.BigIntegerField
db.models.BinaryField
db.models.BinaryField.max_length
db.models.BooleanField
db.models.CASCADE
db.models.CharField
db.models.CharField.db_collation
db.models.CharField.max_length
db.models.CheckConstraint
db.models.CheckConstraint.check
db.models.Count
db.models.Count.distinct
db.models.CursorWrapper.callproc()
db.models.DateField
db.models.DateField.auto_now
db.models.DateField.auto_now_add
db.models.DateTimeField
db.models.DecimalField
db.models.DecimalField.decimal_places
db.models.DecimalField.max_digits
db.models.DO_NOTHING
db.models.DurationField
db.models.EmailField
db.models.Exists
db.models.Expression
db.models.Expression.asc()
db.models.Expression.contains_aggregate
db.models.Expression.contains_over_clause
db.models.Expression.convert_value()
db.models.Expression.desc()
db.models.Expression.empty_result_set_value
db.models.Expression.filterable
db.models.Expression.get_group_by_cols()
db.models.Expression.get_source_expressions()
db.models.Expression.relabeled_clone()
db.models.Expression.resolve_expression()
db.models.Expression.reverse_ordering()
db.models.Expression.set_source_expressions()
db.models.Expression.window_compatible
db.models.expressions.Case
db.models.expressions.RawSQL
db.models.expressions.RowRange
db.models.expressions.RowRange.frame_type
db.models.expressions.ValueRange
db.models.expressions.ValueRange.frame_type
db.models.expressions.When
db.models.expressions.Window
db.models.expressions.Window.template
db.models.ExpressionWrapper
db.models.F
db.models.Field
db.models.Field.auto_created
db.models.Field.blank
db.models.Field.choices
db.models.Field.concrete
db.models.Field.db_column
db.models.Field.db_comment
db.models.Field.db_index
db.models.Field.db_tablespace
db.models.Field.db_type()
db.models.Field.deconstruct()
db.models.Field.default
db.models.Field.description
db.models.Field.descriptor_class
db.models.Field.editable
db.models.Field.error_messages
db.models.Field.formfield()
db.models.Field.from_db_value()
db.models.Field.get_db_prep_save()
db.models.Field.get_db_prep_value()
db.models.Field.get_internal_type()
db.models.Field.get_prep_value()
db.models.Field.help_text
db.models.Field.hidden
db.models.Field.is_relation
db.models.Field.many_to_many
db.models.Field.many_to_one
db.models.Field.model
db.models.Field.null
db.models.Field.one_to_many
db.models.Field.one_to_one
db.models.Field.pre_save()
db.models.Field.primary_key
db.models.Field.rel_db_type()
db.models.Field.related_model
db.models.Field.to_python()
db.models.Field.unique
db.models.Field.unique_for_date
db.models.Field.unique_for_month
db.models.Field.unique_for_year
db.models.Field.validators
db.models.Field.value_from_object()
db.models.Field.value_to_string()
db.models.Field.verbose_name
db.models.fields.files.FieldFile
db.models.fields.files.FieldFile.close()
db.models.fields.files.FieldFile.delete()
db.models.fields.files.FieldFile.name
db.models.fields.files.FieldFile.open()
db.models.fields.files.FieldFile.path
db.models.fields.files.FieldFile.save()
db.models.fields.files.FieldFile.size
db.models.fields.files.FieldFile.url
db.models.fields.json.KT
db.models.fields.related.RelatedManager
db.models.fields.related.RelatedManager.aadd()
db.models.fields.related.RelatedManager.aclear()
db.models.fields.related.RelatedManager.acreate()
db.models.fields.related.RelatedManager.add()
db.models.fields.related.RelatedManager.aremove()
db.models.fields.related.RelatedManager.aset()
db.models.fields.related.RelatedManager.clear()
db.models.fields.related.RelatedManager.create()
db.models.fields.related.RelatedManager.remove()
db.models.fields.related.RelatedManager.set()
db.models.FileField
db.models.FileField.storage
db.models.FileField.upload_to
db.models.FilePathField
db.models.FilePathField.allow_files
db.models.FilePathField.allow_folders
db.models.FilePathField.match
db.models.FilePathField.path
db.models.FilePathField.recursive
db.models.FilteredRelation
db.models.FilteredRelation.condition
db.models.FilteredRelation.relation_name
db.models.FloatField
db.models.ForeignKey
db.models.ForeignKey.db_constraint
db.models.ForeignKey.limit_choices_to
db.models.ForeignKey.on_delete
db.models.ForeignKey.related_name
db.models.ForeignKey.related_query_name
db.models.ForeignKey.swappable
db.models.ForeignKey.to_field
db.models.from_queryset()
db.models.Func
db.models.Func.arg_joiner
db.models.Func.arity
db.models.Func.as_sql()
db.models.Func.function
db.models.Func.template
db.models.functions.Abs
db.models.functions.ACos
db.models.functions.ASin
db.models.functions.ATan
db.models.functions.ATan2
db.models.functions.Cast
db.models.functions.Ceil
db.models.functions.Chr
db.models.functions.Coalesce
db.models.functions.Collate
db.models.functions.Concat
db.models.functions.Cos
db.models.functions.Cot
db.models.functions.CumeDist
db.models.functions.Degrees
db.models.functions.DenseRank
db.models.functions.Exp
db.models.functions.Extract
db.models.functions.ExtractDay
db.models.functions.ExtractHour
db.models.functions.ExtractIsoWeekDay
db.models.functions.ExtractIsoYear
db.models.functions.ExtractMinute
db.models.functions.ExtractMonth
db.models.functions.ExtractQuarter
db.models.functions.ExtractSecond
db.models.functions.ExtractWeek
db.models.functions.ExtractWeekDay
db.models.functions.ExtractYear
db.models.functions.FirstValue
db.models.functions.Floor
db.models.functions.Greatest
db.models.functions.JSONObject
db.models.functions.Lag
db.models.functions.LastValue
db.models.functions.Lead
db.models.functions.Least
db.models.functions.Left
db.models.functions.Length
db.models.functions.Ln
db.models.functions.Log
db.models.functions.Lower
db.models.functions.LPad
db.models.functions.LTrim
db.models.functions.MD5
db.models.functions.Mod
db.models.functions.Now
db.models.functions.NthValue
db.models.functions.Ntile
db.models.functions.NullIf
db.models.functions.Ord
db.models.functions.PercentRank
db.models.functions.Pi
db.models.functions.Power
db.models.functions.Radians
db.models.functions.Random
db.models.functions.Rank
db.models.functions.Repeat
db.models.functions.Replace
db.models.functions.Reverse
db.models.functions.Right
db.models.functions.Round
db.models.functions.RowNumber
db.models.functions.RPad
db.models.functions.RTrim
db.models.functions.SHA1
db.models.functions.SHA224
db.models.functions.SHA256
db.models.functions.SHA384
db.models.functions.SHA512
db.models.functions.Sign
db.models.functions.Sin
db.models.functions.Sqrt
db.models.functions.StrIndex
db.models.functions.Substr
db.models.functions.Tan
db.models.functions.Trim
db.models.functions.Trunc
db.models.functions.TruncDate
db.models.functions.TruncDay
db.models.functions.TruncHour
db.models.functions.TruncMinute
db.models.functions.TruncMonth
db.models.functions.TruncQuarter
db.models.functions.TruncSecond
db.models.functions.TruncTime
db.models.functions.TruncWeek
db.models.functions.TruncYear
db.models.functions.Upper
db.models.GenericIPAddressField
db.models.GenericIPAddressField.protocol
db.models.GenericIPAddressField.unpack_ipv4
db.models.get_lookup()
db.models.get_transform()
db.models.ImageField
db.models.ImageField.height_field
db.models.ImageField.width_field
db.models.Index
db.models.Index.condition
db.models.Index.db_tablespace
db.models.Index.expressions
db.models.Index.fields
db.models.Index.include
db.models.Index.name
db.models.Index.opclasses
db.models.IntegerField
db.models.JSONField
db.models.JSONField.decoder
db.models.JSONField.encoder
db.models.Lookup
db.models.Lookup.lhs
db.models.Lookup.lookup_name
db.models.Lookup.process_lhs()
db.models.Lookup.process_rhs()
db.models.Lookup.rhs
db.models.lookups.RegisterLookupMixin
db.models.lookups.RegisterLookupMixin.get_lookup()
db.models.lookups.RegisterLookupMixin.get_lookups()
db.models.lookups.RegisterLookupMixin.get_transform()
db.models.lookups.RegisterLookupMixin.register_lookup()
db.models.Manager
db.models.Manager.raw()
db.models.ManyToManyField
db.models.ManyToManyField.db_constraint
db.models.ManyToManyField.db_table
db.models.ManyToManyField.limit_choices_to
db.models.ManyToManyField.related_name
db.models.ManyToManyField.related_query_name
db.models.ManyToManyField.swappable
db.models.ManyToManyField.symmetrical
db.models.ManyToManyField.through
db.models.ManyToManyField.through_fields
db.models.Max
db.models.Min
db.models.Model
db.models.Model.__eq__()
db.models.Model.__hash__()
db.models.Model.__str__()
db.models.Model._base_manager
db.models.Model._default_manager
db.models.Model._state
db.models.Model.adelete()
db.models.Model.arefresh_from_db()
db.models.Model.asave()
db.models.Model.clean()
db.models.Model.clean_fields()
db.models.Model.delete()
db.models.Model.from_db()
db.models.Model.full_clean()
db.models.Model.get_absolute_url()
db.models.Model.get_deferred_fields()
db.models.Model.get_FOO_display()
db.models.Model.get_next_by_FOO()
db.models.Model.get_previous_by_FOO()
db.models.Model.objects
db.models.Model.pk
db.models.Model.refresh_from_db()
db.models.Model.save()
db.models.Model.validate_constraints()
db.models.Model.validate_unique()
db.models.OneToOneField
db.models.OneToOneField.parent_link
db.models.Options.abstract
db.models.Options.app_label
db.models.Options.base_manager_name
db.models.Options.constraints
db.models.Options.db_table
db.models.Options.db_table_comment
db.models.Options.db_tablespace
db.models.Options.default_manager_name
db.models.Options.default_permissions
db.models.Options.default_related_name
db.models.Options.get_latest_by
db.models.Options.index_together
db.models.Options.indexes
db.models.Options.label
db.models.Options.label_lower
db.models.Options.managed
db.models.options.Options
db.models.options.Options.get_field()
db.models.options.Options.get_fields()
db.models.Options.order_with_respect_to
db.models.Options.ordering
db.models.Options.permissions
db.models.Options.proxy
db.models.Options.required_db_features
db.models.Options.required_db_vendor
db.models.Options.select_on_save
db.models.Options.unique_together
db.models.Options.verbose_name
db.models.Options.verbose_name_plural
db.models.OuterRef
db.models.output_field
db.models.PositiveBigIntegerField
db.models.PositiveIntegerField
db.models.PositiveSmallIntegerField
db.models.Prefetch
db.models.prefetch_related_objects()
db.models.PROTECT
db.models.Q
db.models.query.QuerySet
db.models.query.QuerySet.aaggregate()
db.models.query.QuerySet.abulk_create()
db.models.query.QuerySet.abulk_update()
db.models.query.QuerySet.acontains()
db.models.query.QuerySet.acount()
db.models.query.QuerySet.acreate()
db.models.query.QuerySet.adelete()
db.models.query.QuerySet.aearliest()
db.models.query.QuerySet.aexists()
db.models.query.QuerySet.aexplain()
db.models.query.QuerySet.afirst()
db.models.query.QuerySet.aget()
db.models.query.QuerySet.aget_or_create()
db.models.query.QuerySet.aggregate()
db.models.query.QuerySet.ain_bulk()
db.models.query.QuerySet.aiterator()
db.models.query.QuerySet.alast()
db.models.query.QuerySet.alatest()
db.models.query.QuerySet.alias()
db.models.query.QuerySet.all()
db.models.query.QuerySet.annotate()
db.models.query.QuerySet.as_manager()
db.models.query.QuerySet.aupdate()
db.models.query.QuerySet.aupdate_or_create()
db.models.query.QuerySet.bulk_create()
db.models.query.QuerySet.bulk_update()
db.models.query.QuerySet.contains()
db.models.query.QuerySet.count()
db.models.query.QuerySet.create()
db.models.query.QuerySet.dates()
db.models.query.QuerySet.datetimes()
db.models.query.QuerySet.db
db.models.query.QuerySet.defer()
db.models.query.QuerySet.delete()
db.models.query.QuerySet.difference()
db.models.query.QuerySet.distinct()
db.models.query.QuerySet.earliest()
db.models.query.QuerySet.exclude()
db.models.query.QuerySet.exists()
db.models.query.QuerySet.explain()
db.models.query.QuerySet.extra()
db.models.query.QuerySet.filter()
db.models.query.QuerySet.first()
db.models.query.QuerySet.get()
db.models.query.QuerySet.get_or_create()
db.models.query.QuerySet.in_bulk()
db.models.query.QuerySet.intersection()
db.models.query.QuerySet.iterator()
db.models.query.QuerySet.last()
db.models.query.QuerySet.latest()
db.models.query.QuerySet.none()
db.models.query.QuerySet.only()
db.models.query.QuerySet.order_by()
db.models.query.QuerySet.ordered
db.models.query.QuerySet.prefetch_related()
db.models.query.QuerySet.raw()
db.models.query.QuerySet.reverse()
db.models.query.QuerySet.select_for_update()
db.models.query.QuerySet.select_related()
db.models.query.QuerySet.union()
db.models.query.QuerySet.update()
db.models.query.QuerySet.update_or_create()
db.models.query.QuerySet.using()
db.models.query.QuerySet.values()
db.models.query.QuerySet.values_list()
db.models.RESTRICT
db.models.SET()
db.models.SET_DEFAULT
db.models.SET_NULL
db.models.signals.class_prepared
db.models.signals.m2m_changed
db.models.signals.post_delete
db.models.signals.post_init
db.models.signals.post_migrate
db.models.signals.post_save
db.models.signals.pre_delete
db.models.signals.pre_init
db.models.signals.pre_migrate
db.models.signals.pre_save
db.models.SlugField
db.models.SlugField.allow_unicode
db.models.SmallAutoField
db.models.SmallIntegerField
db.models.StdDev
db.models.StdDev.sample
db.models.Subquery
db.models.Sum
db.models.Sum.distinct
db.models.TextField
db.models.TextField.db_collation
db.models.TimeField
db.models.Transform
db.models.Transform.bilateral
db.models.Transform.lhs
db.models.Transform.lookup_name
db.models.Transform.output_field
db.models.UniqueConstraint
db.models.UniqueConstraint.condition
db.models.UniqueConstraint.deferrable
db.models.UniqueConstraint.expressions
db.models.UniqueConstraint.fields
db.models.UniqueConstraint.include
db.models.UniqueConstraint.opclasses
db.models.UniqueConstraint.violation_error_message
db.models.URLField
db.models.UUIDField
db.models.Value
db.models.Variance
db.models.Variance.sample
