import pickle


def get_depth_image(filename):

    try:
        pkl_file = open(filename, 'rb')
    except Exception as e:
        raise e

    data = pickle.load(pkl_file)

    pkl_file.close()

    return data[0]['state_before']['depth_image']



def main():

    depth_image = get_depth_image('push_data_06.pkl')
    print depth_image


if __name__ == '__main__':
    main()