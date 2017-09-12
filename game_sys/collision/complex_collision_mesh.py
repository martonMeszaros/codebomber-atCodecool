class ComplexMesh:
    def __init__(self):
        self.meshes = list()

    def __eq__(self, other):
        return isinstance(other, ComplexMesh)

    def add_mesh(self, mesh):
        self.meshes.append(mesh)
