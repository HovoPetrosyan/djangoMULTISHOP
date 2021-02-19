from django.contrib import admin
from Product.models import Category, Product, Images, Comment, Stock
from mptt.admin import DraggableMPTTAdmin


# Register your models here.


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Product,
                                                'category',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Images)


class productImageInline(admin.TabularInline):
    model = Images
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'stock', 'crated_at', 'updated_at', 'image_tag']
    list_filter = ['title', 'crated_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'stock', 'detail']
    prepopulated_fields = {'slug': ('title',)}
    inlines = (productImageInline,)
    save_on_top = True


admin.site.register(Product, ProductAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'status', 'crated_at', 'updated_at', 'user']
    list_filter = ['status', 'crated_at']
    list_per_page = 10


class StockAdmin(admin.ModelAdmin):
    list_display = ['title', 'crated_at', 'updated_at']
    list_filter = ['title']
    list_per_page = 10


admin.site.register(Stock, StockAdmin)

admin.site.register(Comment, CommentAdmin)
