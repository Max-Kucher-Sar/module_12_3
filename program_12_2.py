class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.distance, participant
                    place += 1
                    self.participants.remove(participant)

        """
        С помощью пузырьковой сортировки исправляем логику кода.
        Теперь бегун с меньшей скоростью, и соотвественно меньшей дистанцией никогда
        не займет место выше тех, кто действительно пробежал быстрее.
        """

        final_result = list(finishers.values())
        for i in range(len(final_result)):
            for j in range(len(final_result) - i - 1):
                if final_result[j][0] < final_result[j + 1][0]:
                    final_result[j], final_result[j + 1] = final_result[j + 1], final_result[j]

        result = {}
        place = 1
        for distance, name in final_result:
            result[place] = name
            place += 1


        return result