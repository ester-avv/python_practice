def study_schedule(permanence_period, target_time):
    try:
        period = 0
        for p_start, p_end in permanence_period:
            if p_start <= int(target_time) <= p_end:
                period += 1
        return period
    except TypeError:
        return None


"""     raise NotImplementedError """
