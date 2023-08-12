def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int) or not isinstance(
        permanence_period, list
    ):
        return None
    period = 0
    for p_start, p_end in permanence_period:
        try:
            if p_start <= int(target_time) <= p_end:
                period += 1
        except TypeError:
            return None
    return period
    raise NotImplementedError
