class ScoreProcessor:

    def process_score_file(self, file_path: str) -> int:
        file = None
        try:
            file = open(file_path, "r")
            content = file.read().strip()
            score = int(content)

        except FileNotFoundError:
            print(f"Error: File '{file_path}' was not found.")
            raise

        except ValueError:
            print(f"Error: File '{file_path}' contains invalid data — expected an integer.")
            raise

        else:
            print("Data processed successfully.")
            return score * 10

        finally:
            if file:
                file.close()
            print("File cleanup completed.")