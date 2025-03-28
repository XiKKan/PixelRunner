import numba


@numba.njit(cache=True)
def _get_scale_factor(s_size, o_size) -> float:
    return s_size / o_size


@numba.njit(cache=True)
def _get_scale_factor_x_y(s_size_x, s_size_y, o_size_x, o_size_y):
    return s_size_x / o_size_x, s_size_y / o_size_y


@numba.njit(cache=True)
def _get_speed(speed, scale_factor) -> float:
    return speed * scale_factor
