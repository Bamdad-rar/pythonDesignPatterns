from builder import Builder


class DirectorA:
    @staticmethod
    def construct():
        return Builder().build_part_a().build_part_b().build_part_c().get_result()


class DirectorB:
    @staticmethod
    def construct():
        return Builder().build_part_b().build_part_c().get_result()

