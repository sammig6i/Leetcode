class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, content = log.split(" ", 1)
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((content, identifier, log))

        letter_logs.sort(key=lambda x: (x[0], x[1]))

        ordered_logs = [log[2] for log in letter_logs] + digit_logs

        return ordered_logs