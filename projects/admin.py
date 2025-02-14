from django.contrib import admin
from .models import Project, InstructionManual

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Information", {
            'fields': ('name',)
        }),
        ("Image Fields", {
            'fields': (
                'original_image',
                'cropped_image',
                'interpolated_image',
                'quantized_image',
                'final_image',
            )
        }),
        ("Major Settings", {
            'fields': ('plate_width',)
        }),

        ("Step 1 Settings", {
            'fields': (
                'resolution_width',
                'resolution_height',
            )
        }),

        ("Step 2 Settings", {
            'fields': (
                'interpolation_algorithm',
                'hue_adjustment',
                'saturation_adjustment',
                'value_adjustment',
            )
        }),

        ("Step 3 Settings", {
            'fields': (
                'pixel_piece',
                'color_distance_function',
                'quantization_algorithm',
                'tiebreak_techniques',
                'blocking_factor',
                'piece_availability',
                'has_unlimited_pieces',
            )
        }),
        
        ("Step 4 Settings", {
            'fields': (
                'pieces_used',
                'bricklink_xml',
            )
        }),
    )

@admin.register(InstructionManual)
class InstructionManualAdmin(admin.ModelAdmin):
    pass
