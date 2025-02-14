from django.db import models

PLATE_WIDTH_CHOICES = [
    ('8x8', '8x8'),
    ('16x16', '16x16'),
]

INTERPOLATION_ALGORITHM_CHOICES = [
    ('default', 'Browser Default'),
    ('average', 'Average Pooling'),
    ('dual_min_max', 'Dual Min Max Pooling'),
    ('min', 'Min Pooling'),
    ('max', 'Max Pooling'),
]

PIXEL_PIECE_CHOICES = [
    ('1x1_round_tile', '1x1 Round Tile'),
    ('1x1_round_plate', '1x1 Round Plate'),
    ('1x1_square_tile', '1x1 Square Tile'),
    ('1x1_square_plate', '1x1 Square Plate'),
    ('1x1_square_brick', '1x1 Square Brick'),
    ('variable_tile', 'Variable Tile'),
    ('variable_plate', 'Variable Plate'),
    ('variable_brick', 'Variable Brick'),
]

COLOR_DISTANCE_FUNCTION_CHOICES = [
    ('euclideanRGB', 'Euclidean RGB'),
    ('euclideanLAB', 'Euclidean LAB'),
    ('cie94', 'CIE94'),
    ('ciede2000', 'CIEDE2000'),
    ('din99o', 'DIN99o'),
]

QUANTIZATION_ALGORITHM_CHOICES = [
    ('twoPhase', '2 Phase'),
    ('floydSteinberg', 'Floyd-Steinberg Dithering'),
    ('jarvisJudiceNinkeDithering', 'Jarvis-Judice-Ninke Dithering'),
    ('atkinsonDithering', 'Atkinson Dithering'),
    ('sierraDithering', 'Sierra Dithering'),
    ('greedy', 'Greedy'),
    ('greedyWithDithering', 'Greedy Gaussian Dithering'),
]

TIEBREAK_TECHNIQUE_CHOICES = [
    ("none", "None"),
    ("random", "Random"),
    ("mod2", "Mod 2"),
    ("mod3", "Mod 3"),
    ("mod4", "Mod 4"),
    ("mod5", "Mod 5"),
    ("noisymod2", "Noisy Mod 2"),
    ("noisymod3", "Noisy Mod 3"),
    ("noisymod4", "Noisy Mod 4"),
    ("noisymod5", "Noisy Mod 5"),
    ("cascadingmod", "Cascading Mod"),
    ("cascadingnoisymod", "Cascading Noisy Mod"),
    ("alternatingmod", "Alternating Mod"),
    ("alternatingnoisymod", "Alternating Noisy Mod"),
]

# TODO: Add support for saving 3D settings
class Project(models.Model):
    name = models.CharField(max_length=100)

    # Image Fields
    original_image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    cropped_image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    interpolated_image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    quantized_image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    final_image = models.ImageField(upload_to="project_images/", blank=True, null=True)

    # Major settings
    plate_width = models.CharField(choices=PLATE_WIDTH_CHOICES, default='8x8', max_length=20)

    # Step 1 settings
    resolution_width = models.PositiveSmallIntegerField()
    resolution_height = models.PositiveSmallIntegerField()

    # Step 2 settings
    interpolation_algorithm = models.CharField(max_length=20, choices=INTERPOLATION_ALGORITHM_CHOICES)
    hue_adjustment = models.SmallIntegerField(default=0)
    saturation_adjustment = models.SmallIntegerField(default=0)
    value_adjustment = models.SmallIntegerField(default=0)

    # Step 3 settings
    pixel_piece = models.CharField(max_length=50, choices=PIXEL_PIECE_CHOICES)
    color_distance_function = models.CharField(max_length=50, choices=COLOR_DISTANCE_FUNCTION_CHOICES)
    quantization_algorithm = models.CharField(max_length=50, choices=QUANTIZATION_ALGORITHM_CHOICES)
    tiebreak_techniques = models.CharField(max_length=50, choices=TIEBREAK_TECHNIQUE_CHOICES)
    blocking_factor = models.PositiveSmallIntegerField(default=0)
    piece_availability = models.JSONField(blank=True, null=True)
    has_unlimited_pieces = models.BooleanField(default=True)

    # Step 4 settings
    pieces_used = models.JSONField(blank=True, null=True)
    bricklink_xml = models.TextField(blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InstructionManual(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='instruction_manuals')
    rendered_pdf = models.FileField(upload_to="instruction_manuals/", blank=True, null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project) + " Instruction Manual"













