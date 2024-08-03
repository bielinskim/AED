import pandas as pd


def load_data():
    data = []

    with open('ad.names', 'r') as file:
        lines = file.readlines()
        feature_names = [line.split(':')[0] for line in lines[3:] if ':' in line]
    feature_names.append('class')
    data.append(feature_names)

    with open('ad.data', 'r') as file:
        for line in file:

            line = line.strip()

            row = line.split(',')

            data.append(row)

    df = pd.DataFrame(data)


    df.to_csv('output.csv', index=False, header=False)

    print('Finished')


if __name__ == '__main__':
    load_data()

