import cadquery as cq

# Holder
holder_width = 14

# Base
height = 65
width = 354 - (holder_width * 2)
thickness = 2.5
fillet_value = 1.5

# Grate
grate_width = width
slot_width = 1.5
slot_spacing = 4
slot_height = int(height/4)
count_slots = int(grate_width / (slot_width + slot_spacing))

# Bee entry
entry_slot_width = 6
entry_slot_spacing = 6
entry_slot_height = 10
count_entry_slots = 8

# Handle
handle_width = 5
handle_length = 20
handle_height = 10

# holder_width = 14
holder_extra_width = 14
holder_height = height
holder_thickness = thickness

###
# Create entrance reducer holders
###

result = cq.Workplane("front").box(holder_height, holder_width, holder_thickness).tag("base_front") # Create Workplane
# holder = holder.faces(">Z").tag("base_front") # Create Workplane

###
# Create the extra holder
###
result = result.faces(">Y").workplane().center(0,holder_thickness/4).rect(holder_height, holder_thickness/2).extrude(holder_extra_width)

###
# Add the screw holes
###
result = result.faces(">Z").workplane().center(int(holder_height/4),-(holder_width+holder_extra_width)/4).cskHole(diameter=2.4, cskDiameter=4.4, cskAngle=82, depth=holder_thickness)
result = result.faces(">Z").workplane().center(-int(holder_height/2),0).cskHole(diameter=2.4, cskDiameter=4.4, cskAngle=82, depth=holder_thickness)


###
# Render the object
###
show_object(result)
# highlight_object(holder)

###
# Exports
###
cq.exporters.export(result,'out/bracket.stl')
# cq.exporters.export(result,'out/bracket.svg')
# cq.exporters.export(result.section(),'out/bracket.dxf')
# cq.exporters.export(result,'out/bracket.step')