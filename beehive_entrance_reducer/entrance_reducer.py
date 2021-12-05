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

# print("Count slots:", count_slots)

# make the base
# result = cq.Workplane("front").box(height, width, thickness) # Create Workplane
entrance_reducer = cq.Workplane("front").box(height, width, thickness) # Create Workplane

# Round the edges
entrance_reducer = entrance_reducer.edges("|Z").fillet(fillet_value) # Select edges with parallel to Z dir and apply a fillet

# Tag the workplane for later
entrance_reducer = entrance_reducer.faces(">Z").workplane().tag("base_z")

# Add the slots
# Select Face farthest in the positive Z dir and move down half way and create slots
entrance_reducer = entrance_reducer.center(height/2-slot_height,0).rarray(1,slot_spacing,1,count_slots).slot2D(slot_height,slot_width,0).cutThruAll()

###
# Add the bee entry
###
entrance_reducer = entrance_reducer.faces(">Z").center(-((height/2-slot_height)+(height/2)),0).rarray(1,entry_slot_spacing*2,1,count_entry_slots).slot2D(entry_slot_height*2,entry_slot_width,0).cutThruAll()

###
# Add handles
###
entrance_reducer = entrance_reducer.workplaneFromTagged("base_z").center(-handle_length/2,-width/3.25).circle(handle_length/2).workplane(offset=handle_height/2).rect(handle_width, handle_length).workplane(offset=handle_height/2).rect(handle_width, handle_length).loft(combine=True)
entrance_reducer = entrance_reducer.workplaneFromTagged("base_z").center(-handle_length/2,width/3.25).circle(handle_length/2).workplane(offset=handle_height/2).rect(handle_width, handle_length).workplane(offset=handle_height/2).rect(handle_width, handle_length).loft(combine=True)

###
# Cut the model in half along the Y axis
###
left = entrance_reducer.faces(">Y").workplane(-width/2).split(keepTop=True, keepBottom=False)
right = entrance_reducer.faces(">Y").workplane(-width/2).split(keepTop=False, keepBottom=True)

###
# Render the object
###
show_object(entrance_reducer)

###
# Exports
###
cq.exporters.export(left,'out/beehive_entrance_reducer_left.stl')
cq.exporters.export(right,'out/beehive_entrance_reducer_right.stl')
# cq.exporters.export(result,'out/beehive_entrance_reducer.svg')
# cq.exporters.export(result.section(),'out/beehive_entrance_reducer.dxf')
# cq.exporters.export(result,'out/beehive_entrance_reducer.step')
