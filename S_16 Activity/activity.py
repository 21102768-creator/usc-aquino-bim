import ifcopenshell

ifc_file = ifcopenshell.open("AC20-FZK-Haus.ifc")
#3
print("IFC file loaded:", ifc_file.schema)
print()
#4
project = ifc_file.by_type("IfcProject")[0]
print("Project Name:", project.Name)
print()
#5
stairs = ifc_file.by_type("IfcStair")
print(f"Number of stairs: {len(stairs)}")

for stair in stairs:
	print(stair.GlobalId, stair.Name)
print()
#6
slabs = ifc_file.by_type("IfcSlab")

print(f"Number of slabs: {len(slabs)}")

for slab in slabs:
	print(slab.GlobalId, slab.Name)
print()
#7
for i, slab in enumerate(slabs, 1):
    slab.Name = f"Renamed_Slab_{i}"
    print(f"Updated slab: {slab.GlobalId} → {slab.Name}")
print()
#8
print("Spatial Structure:")
project = ifc_file.by_type("IfcProject")[0]

for site in project.IsDecomposedBy[0].RelatedObjects:
 
    for building in site.IsDecomposedBy[0].RelatedObjects:
       
        for storey in building.IsDecomposedBy[0].RelatedObjects:
            print("storey",storey.Name,"Elevation", storey.Elevation)
print()      	
#9
types = set(el.is_a() for el in ifc_file)
print("Object types in file:",types)
print()
#10
ifc_file.write("AC20-FZK-Haus_renamed.ifc")
print(f"Saved renamed slabs to: AC20-FZK-Haus_renamed.ifc")
