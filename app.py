import src.v1 as version_1
import src.v2 as version_2



if __name__ == '__main__':
    build_version = 1

    if build_version == 1:
        version_1.run()
    elif build_version == 2:
        version_2.run()
